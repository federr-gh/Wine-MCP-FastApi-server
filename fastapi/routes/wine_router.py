from fastapi import APIRouter
from model.wine_model import Wine
import numpy as np
from fastapi import HTTPException
import pickle
import os

router = APIRouter()

MODEL_PATH = os.path.join(os.path.dirname(__file__), "Regression.pkl")

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Model file not found or corrupted: {e}")

@router.post("/Wines")
async def get_wines(wine: Wine):
    """
    Returns a list of wines with their respective features.
    """
    
    """
    wines = [
        {"id": 1, "name": "Wine A", "features": [7.4, 0.7, 0.0, 1.9, 0.076, 11.4, 34, 0.9978, 3.51, 0.56]},
        {"id": 2, "name": "Wine B", "features": [7.8, 0.88, 0.0, 2.6, 0.075, 12.8, 67, 0.9968, 3.2, 0.68]},
        # Add more wines as needed
    ]
    """
    wine_array = np.array([list(wine.model_dump().values())]).reshape(1, -1)
    try:
        pred = model.predict(wine_array)
        return {'wine': int(pred[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")