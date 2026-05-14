from pydantic import BaseModel
from typing import Optional


class RecommendationRequest(BaseModel):
    date: Optional[str] = None
    channel: Optional[str] = None
    audience_segment: Optional[str] = None


class RecommendationResponse(BaseModel):
    model_name: str
    model_version: str
    recommendation: Optional[str] = None
    expected_incremental_value: Optional[float] = None
