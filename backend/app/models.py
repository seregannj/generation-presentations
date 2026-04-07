# backend/app/models.py
from pydantic import BaseModel
from typing import Literal


class ReportRequest(BaseModel):
    topic: str
    style: Literal["academic", "casual", "business", "creative"] = "academic"
    word_count: int = 500


class TextResponse(BaseModel):
    content: str
    word_count: int
