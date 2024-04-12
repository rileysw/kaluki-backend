from pydantic import BaseModel

class Hand(BaseModel):
    user: str
    hand: list
