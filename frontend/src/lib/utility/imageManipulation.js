// Most functions generated with claude sonnet 3.7 and small changes by myself.
export function convertToGrayscale(pixels, width, height) {
  const grayscale = new Uint8ClampedArray(width * height);

  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const idx = (y * width + x) * 4;

      // Extract RGBA values
      const red = pixels[idx];
      const green = pixels[idx + 1];
      const blue = pixels[idx + 2];
      const alpha = pixels[idx + 3];

      // Calculate grayscale intensity using a weighted average
      // Common weights: 0.299 for red, 0.587 for green, 0.114 for blue
      const intensity = 0.299 * red + 0.587 * green + 0.114 * blue;

      // Optionally, factor in alpha (e.g., scale intensity by alpha/255)
      const adjustedIntensity = intensity * (alpha / 255);

      // Assign the grayscale value to the output array
      grayscale[y * width + x] = adjustedIntensity;
    }
  }

  return grayscale;
}

// This was used because my first approach was to use a 500x500 canvas. But this led to a weird behaviour of the
//   prediction. I assume that is because the pixels weren't captured correctly.
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