from pydantic import BaseModel
from typing import Optional

class Image(BaseModel):
    image_base64: str
