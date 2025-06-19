from pydantic import BaseModel
from typing import Dict

class Evaluation(BaseModel):
    userId: int
    ratings: Dict[str, int]