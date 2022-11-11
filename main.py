import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, Body
from sqlalchemy.orm import Session

import crud
import models
import schemas
from analyse import findRankName, analyseHandRank
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/compareHands")
async def compareHands(info : Request):
    best_hand, best_rank = await crud.processHands(info)

    return {
        "status" : "SUCCESS",
        "bestHand" : best_hand,
        "bestRank" : best_rank
    }

@app.post("/randomhand/")
def create_random_hand(db: Session = Depends(get_db)):
    return crud.create_random_hand(db=db)

@app.post("/hand/")
def create_hand(hand: schemas.Hand, db: Session = Depends(get_db)):
    hand, rank = crud.create_hand(db=db, hand=hand)
    rankName = findRankName(rank)
    return hand, rankName

@app.get("/hands/", response_model=list[schemas.Hand])
def read_hands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hands = crud.get_hands(db, skip=skip, limit=limit)
    return hands

@app.get("/hand/{hand_id}", response_model=schemas.Hand) #Should be Hand?
def read_hand(hand_id: int, db: Session = Depends(get_db)):
    db_hand = crud.get_hand(db, hand_id=hand_id)
    if db_hand is None:
        raise HTTPException(status_code=404, detail="Hand not found")
    return db_hand


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
