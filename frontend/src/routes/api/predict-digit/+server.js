import { json } from '@sveltejs/kit';

export async function POST({ request }) {
  try {
    const { imageData } = await request.json();

    console.log("\nHello from server")
    console.log(JSON.stringify({ greyscale_image: imageData }))
    // TODO call backend instead of ML service
    const response = await fetch('http:localhost:4242/predict-handwritten-digit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ greyscale_image: imageData })
    });


    const prediction = await response.json();

    // Return the prediction data
    return json(prediction);
  } catch (error) {
    console.error('Error in predict endpoint:', error);
    return json({ error: 'Failed to process prediction' }, { status: 500 });
  }
}