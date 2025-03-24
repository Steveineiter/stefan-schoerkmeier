# Best practices from https://github.com/pytorch/examples/blob/main/mnist/main.py aka official pytroch MNIST solution.
import argparse
import time

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR


class ConvolutionalNetwork(nn.Module):
    def __init__(self):
        super(ConvolutionalNetwork, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, 1)
        self.conv2 = nn.Conv2d(16, 32, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        # Input: conv1: 28-3+1 => 26x26x16 pooling => 13x13 conv2: 13-3+1 => 11x11x32 pooling => 5x5x32 = 800
        self.fc1 = nn.Linear(800, 64)
        self.fc2 = nn.Linear(64, 10)  # 10 classes (0, 1, 2, ... 9)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)

        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))

        output = F.log_softmax(x, dim=1)
        return output

def train(args, model, optimizer, device, train_loader, epoch):
    model.train()
    for batch_index, (images, labels) in enumerate(train_loader):
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()

        outputs = model(images)
        # Since we are already doing a log_softmax, negative log likelihood should be more efficient than
        #   using cross entropy.
        loss = F.nll_loss(outputs, labels)
        loss.backward()
        optimizer.step()

        if batch_index % args.log_interval == 0:
            print(f"Train Epoch: {epoch} "
                  f"[{batch_index * len(images)}/{len(train_loader.dataset)} "
                  f"({100 * batch_index / len(train_loader):.0f}%)] "
                  f"Loss: {loss.item():.4f}")
        elif (batch_index + 1) == len(train_loader):
            print(f"Train Epoch: {epoch} "
                  f"[{len(train_loader.dataset)}/{len(train_loader.dataset)} (100%)] "
                  f"Loss: {loss.item():.4f}")

def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct_predictions = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            test_loss += F.nll_loss(outputs, labels, reduction="sum").item()  # Sum up batch loss

            predicted = torch.max(outputs.data, 1)[1]
            correct_predictions += (predicted == labels).sum()

    test_loss /= len(test_loader.dataset)
    print(f"\nTest set: Loss: {test_loss:.4f}, Accuracy: {correct_predictions / len(test_loader.dataset):.4f}")

def _args():
    parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                        help='input batch size for training (default: 64)')
    parser.add_argument('--test-batch-size', type=int, default=512, metavar='N',
                        help='input batch size for testing (default: 512)')
    parser.add_argument('--epochs', type=int, default=5, metavar='N',
                        help='number of epochs to train (default: 5)')
    parser.add_argument('--lr', type=float, default=1, metavar='LR',
                        help='learning rate (default: 1)')
    parser.add_argument('--gamma', type=float, default=0.7, metavar='M',
                        help='learning rate step gamma (default: 0.7)')
    parser.add_argument('--seed', type=int, default=1, metavar='S',
                        help='random seed (default: 1)')
    parser.add_argument('--log-interval', type=int, default=100, metavar='N',
                        help='how many batches to wait before logging training status')
    parser.add_argument('--save-model', action='store_true', default=False,
                        help='flag whether the current model should be saved')
    return parser.parse_args()


def main():
    args = _args()
    torch.manual_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    transform = transforms.Compose([
        transforms.ToTensor(),
        # Mean and std of the MNIST dataset. We can calculate those values by checking out all pixels. But those are
        #   common numbers to use.
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    train_data = datasets.MNIST('../data', train=True, download=True, transform=transform)
    test_data = datasets.MNIST('../data', train=False, transform=transform)

    train_kwargs = {'batch_size': args.batch_size}
    test_kwargs = {'batch_size': args.test_batch_size}
    if torch.cuda.is_available():
        cuda_kwargs = {'num_workers': 1,
                       'pin_memory': True,
                       'shuffle': True}
        train_kwargs.update(cuda_kwargs)
        test_kwargs.update(cuda_kwargs)
    train_loader = DataLoader(train_data, **train_kwargs)
    test_loader = DataLoader(test_data, **test_kwargs)

    model = ConvolutionalNetwork().to(device)
    optimizer = torch.optim.Adadelta(model.parameters(), lr=args.lr)
    scheduler = StepLR(optimizer, step_size=1, gamma=args.gamma)
    start_time = time.time()
    for epoch in range(1, args.epochs + 1):
        train(args, model, optimizer, device, train_loader, epoch)
        test(model, device, test_loader)
        scheduler.step()
    print(f"Duration of training: {(time.time() - start_time) / 60} minutes.")

    if args.save_model:
        torch.save(model.state_dict(), "../models/handwritten_digit_classifier.pt")

if __name__ == '__main__':
    main()
