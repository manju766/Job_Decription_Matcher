from pydantic import BaseModel
from typing import List

class MatchRequest(BaseModel):
    resume: str
    job_description: str

class MatchResponse(BaseModel):
    match_score: float
    missing_keywords: List[str]
