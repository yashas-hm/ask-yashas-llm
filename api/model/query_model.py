from typing import Optional

from pydantic import BaseModel


class QueryModel(BaseModel):
    query: str
    history: Optional[list] = []
