from fastapi import APIRouter, Request, HTTPException
import requests
from starlette import status

from app.self_hosted_machine_learning.schemas import GrayscaleImage, PredictionResponse
self_hosted_machine_learning_router = APIRouter(prefix="/ml", tags=["ml"])
MODEL_URL = "http://localhost:4242/predict-handwritten-digit"

@self_hosted_machine_learning_router.post(
    "/predict",
    status_code=status.HTTP_200_OK,
    response_model=PredictionResponse,
)
async def predict_digit(
    grayscale_image: GrayscaleImage,
):
    headers = {"Content-Type": "application/json"}
    payload = {"grayscale_image": grayscale_image.greyscale_image}
    try:
        response = requests.post(MODEL_URL, headers=headers, json=payload)
    except requests.exceptions.ConnectionError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Connection to machine learning server could not be established."
        )
    return PredictionResponse(prediction=response.json()["prediction"])