import torch
import uvicorn
from fastapi import FastAPI
from starlette import status

from app.schemas import GrayscaleImage, PredictionResponse
# from schemas import GrayscaleImage, PredictionResponse  # For debugging, pycharm has a complaint xD

from scripts.training_mnist_recognition import ConvolutionalNetwork

app = FastAPI(
    # TODO as soon as we deploy we have to comment those in.
    # docs_url=None,
    # redoc_url=None,
)

# TODO add in full product
# app.add_middleware()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = ConvolutionalNetwork().to(device)
model.load_state_dict(torch.load("models/handwritten_digit_classifier.pt", map_location=device))
model = model.to(device)
model.eval()


@app.post("/predict-handwritten-digit",
          status_code=status.HTTP_200_OK,
          response_model=PredictionResponse,
)
async def predict_handwritten_digit(grayscale_image: GrayscaleImage, ):
    input_image = torch.tensor(grayscale_image.greyscale_image, device=device).unsqueeze(0).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(input_image)

    prediction = torch.max(output.data, 1)[1]
    return PredictionResponse(
        prediction=prediction.item())

@app.get("/healthy")
def health_check():
    return {"status": "healthy"}


# Used to debug in pycharm.
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=4242)