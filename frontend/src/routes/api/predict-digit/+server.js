import { json } from '@sveltejs/kit';
import { env } from '$env/dynamic/private';

export async function POST({ request }) {
 const backendUrl = env.BACKEND_URL || 'http://localhost:8080';

  try {
    const { imageData } = await request.json();
    // console.log(JSON.stringify({ greyscale_image: imageData }))

    // TODO call backend instead of ML service
    const response = await fetch(`${backendUrl}/ml/predict`, {
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
    console.error('Server: Error in predict endpoint:', error);
    return json({ error: 'Server: Failed to process prediction' }, { status: 500 });
  }
}