from pydantic import BaseModel, Field
from typing import List

class PRModel(BaseModel):
    title: str = Field(min_length=5, max_length=72)
    summary: str
    changes: List[str]
    testing: str
    risk: str
    checklist: List[str]
