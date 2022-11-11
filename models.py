from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Hand(Base):
    __tablename__ = "hands"

    id = Column(Integer, primary_key=True, index=True)
    card_1 = Column(String)
    card_2 = Column(String)
    card_3 = Column(String)
    card_4 = Column(String)
    card_5 = Column(String)

