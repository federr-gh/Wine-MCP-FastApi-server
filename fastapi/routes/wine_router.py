from fastapi import APIRouter
from models.wine_model import Wine
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

@router.post("/Wines", operation_id='get_wine_class')
async def get_wines(wine: Wine):
    """
    Returns a list of wines with their respective features.
    """
    wine_array = np.array([list(wine.model_dump().values())]).reshape(1, -1)
    try:
        pred = model.predict(wine_array)
        return {'wine': int(pred[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")