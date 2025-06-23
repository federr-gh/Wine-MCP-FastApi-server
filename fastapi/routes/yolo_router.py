from ultralytics import YOLO
import os
from fastapi import APIRouter
from fastapi import HTTPException
from models.image_model import Image

router = APIRouter()

MODEL_PATH = os.path.join(os.path.dirname(__file__), "best.pt")

@router.post("/Yolo", operation_id='get_marsupial')
async def get_marsupial(image: Image):
    """
    Returns a predict of marsupial.
    """
    try:
        model = YOLO(MODEL_PATH)
        pred = model.predict(image.image_base64)
        boxes = pred[0].boxes
        if boxes is None or len(boxes) == 0:
            return {"marsupial": "No detection"}

        results = []
        for box in boxes:
            class_id = int(box.cls[0])
            class_name = pred[0].names[class_id]
            results.append(class_name)

        return {"marsupials": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")