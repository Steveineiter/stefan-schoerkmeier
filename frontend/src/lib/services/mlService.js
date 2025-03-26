// lib/services/mlService.js
export async function predictNumber(imageData) {
  try {
    const response = await fetch('/api/predict-digit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ imageData })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error("Error predicting number:", error);
    throw error;
  }
}
