from pydantic import BaseModel
from typing import Optional


class ReportRequest(BaseModel):
    topic: str
    style: str = "academic"
    word_count: int = 500
    additional: Optional[str] = None


class TextResponse(BaseModel):
    content: str
    word_count: int
