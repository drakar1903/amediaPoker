from pydantic import BaseModel


class HandBase(BaseModel):
    id: int


class Hand(HandBase):
    card_1: str
    card_2: str
    card_3: str
    card_4: str
    card_5: str

    class Config:
        orm_mode = True
