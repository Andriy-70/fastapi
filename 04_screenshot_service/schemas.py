from pydantic import BaseModel, Field
from datetime import datetime

class ScreenshotCreate(BaseModel):
    url: str = Field(min_length=8, max_length=100)

class ScreenshotResponse(BaseModel):
    id: int
    url: str
    screenshot_path: str
    created_at: datetime

    model_config = {"from_attributes": True} # беремо об'єкт із бази