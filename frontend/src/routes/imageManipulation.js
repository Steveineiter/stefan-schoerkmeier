// Most functions generated with claude sonnet 3.7 and small changes by myself.
export function convertToGrayscale(pixels, width, height) {
  const grayscale = new Uint8ClampedArray(width * height);

  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const idx = (y * width + x) * 4;

      // Check alpha value (pixels[idx + 3])
      // If alpha is high (opaque), set to black (0)
      // If alpha is low (transparent), set to white (255)
      const alpha = pixels[idx + 3];

      // You might want to adjust this threshold based on your drawing
      const threshold = 128;

      if (alpha > threshold) {
        grayscale[y * width + x] = 0;  // Black

        // Debug output for the first few detected pixels
        if (grayscale[y * width + x] === 0) {
          console.log("Found black pixel at", x, y, "with alpha", alpha);
        }
      } else {
        grayscale[y * width + x] = 255;  // White
      }
    }
  }

  return grayscale;
}

export function resizeImage(pixels, origWidth, origHeight, newWidth, newHeight) {
  // Create new array for the resized image
  const resized = new Uint8ClampedArray(newWidth * newHeight);

  // Calculate the exact scaling ratio
  const xRatio = origWidth / newWidth;
  const yRatio = origHeight / newHeight;

  for (let y = 0; y < newHeight; y++) {
    for (let x = 0; x < newWidth; x++) {
      // Calculate the starting pixel coordinates in the original image
      const srcX = Math.floor(x * xRatio);
      const srcY = Math.floor(y * yRatio);

      // Calculate the ending pixel coordinates to define our window
      const endX = Math.min(Math.floor((x + 1) * xRatio), origWidth);
      const endY = Math.min(Math.floor((y + 1) * yRatio), origHeight);

      // Max pooling - find any black/dark pixel in the region
      let hasContent = false;

      // Sample from the appropriate window in the original image
      for (let sy = srcY; sy < endY && !hasContent; sy++) {
        for (let sx = srcX; sx < endX && !hasContent; sx++) {
          // If pixel is "dark" (below threshold), mark as content
          // Assuming your input pixels is single-channel grayscale where 0 is black
          if (pixels[sy * origWidth + sx] < 128) {  // Using middle threshold (you can adjust)
            hasContent = true;
            break;
          }
        }
      }

      // Set to black (0) if content was found, white (255) otherwise
      resized[y * newWidth + x] = hasContent ? 0 : 255;
    }
  }

  return resized;
}


export function convertDictTo2DListWithValues(dictionary, rows = 28, columns = 28, defaultValue = -0.4242) {
  // Create a 2D array initialized with the default value
  const result = Array(rows).fill().map(() => Array(columns).fill(defaultValue));

  // Fill in values from the dictionary
  for (const [key, value] of Object.entries(dictionary)) {
    // Convert key to integer and subtract 1 for 0-based indexing
    const idx = parseInt(key);

    // Calculate row and column
    const row = Math.floor(idx / columns);
    const col = idx % columns;

    // Update the value if within bounds
    if (row < rows && col < columns) {
      result[row][col] = value;
    }
  }

  return result;
}