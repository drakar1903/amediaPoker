from sqlalchemy.orm import Session

import cards
import models
import schemas
from analyse import analyseHandRank


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_hand(db: Session, hand_id: int):
    return db.query(models.Hand).filter(models.Hand.id == hand_id).first()


def get_hands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hand).offset(skip).limit(limit).all()

async def processHands(info):
    req_info = await info.json()
    best_hand = ""
    best_rank = 100
    for hand in req_info:
        print(hand)
        givenHand = []
        print(givenHand)
        givenHand.append(hand.get("card_1"))
        givenHand.append(hand.get("card_2"))
        givenHand.append(hand.get("card_3"))
        givenHand.append(hand.get("card_4"))
        givenHand.append(hand.get("card_5"))
        rank = analyseHandRank(givenHand)
        print("Handrank: ", rank)
        if rank < best_rank:
            best_hand = givenHand
            best_rank = rank
    return best_hand, best_rank



def create_random_hand(db: Session):
    hand = cards.generateRandomHand()
    rank = analyseHandRank(hand)
    print(hand)
    print("Handrank: ", rank)
    db_hand = models.Hand(card_1=hand[0],
                          card_2=hand[1],
                          card_3=hand[2],
                          card_4=hand[3],
                          card_5=hand[4], )
    db.add(db_hand)
    db.commit()
    db.refresh(db_hand)
    return db_hand


def create_hand(db: Session, hand: schemas.Hand):
    givenHand = []
    print(givenHand)
    givenHand.append(hand.card_1)
    givenHand.append(hand.card_2)
    givenHand.append(hand.card_3)
    givenHand.append(hand.card_4)
    givenHand.append(hand.card_5)
    rank = analyseHandRank(givenHand)
    db_hand = models.Hand(card_1=hand.card_1,
                          card_2=hand.card_2,
                          card_3=hand.card_3,
                          card_4=hand.card_4,
                          card_5=hand.card_5)
    db.add(db_hand)
    db.commit()
    db.refresh(db_hand)
    return db_hand, rank