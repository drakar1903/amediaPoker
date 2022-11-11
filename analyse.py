

def analyseHandRank(hand):
    ranking = 0
    if isStraight(hand) and isFlush(hand):
        ranking = 1
    elif isFour(hand):
        ranking = 2
    elif isFullHouse(hand):
        ranking = 3
    elif isFlush(hand):
        ranking = 4
    elif isStraight(hand):
        ranking = 5
    elif isThree(hand):
        ranking = 6
    elif isTwoPair(hand):
        ranking = 7
    elif isOnePair(hand):
        ranking = 8
    else:
        ranking = 9
    return ranking

def findRankName(rank):
    if rank == 1:
        return "Straight Flush"
    elif rank == 2:
        return "Four of a kind"
    elif rank == 3:
        return "Full House"
    elif rank == 4:
        return "Flush"
    elif rank == 5:
        return "Straight"
    elif rank == 6:
        return "Three of a kind"
    elif rank == 7:
        return "Two pair"
    elif rank == 8:
        return "One pair"
    else:
        return "High card"



def getJustValues(hand):
    cardValue = int(0)
    hv = []
    for card in hand:
        if card[0] == 't':
            cardValue = int(10)
        elif card[0] == 'j':
            cardValue = int(11)
        elif card[0] == 'q':
            cardValue = int(12)
        elif card[0] == 'k':
            cardValue = int(13)
        elif card[0] == 'a':
            cardValue = int(14)
        else:
            cardValue = int(card[0])
        hv.append(cardValue)
    return hv

def isOnePair(hand):
    hv = getJustValues(hand)
    hv.sort()
    # pair card card card
    if hv[0] == hv[1] and hv[1] != hv[2] and hv[2] != hv[3] and hv[3] != hv[4]:
        return True
    # card pair card card
    if hv[0] != hv[1] and hv[1] == hv[2] and hv[2] != hv[3] and hv[3] != hv[4]:
        return True
    # card card pair card
    if hv[0] != hv[1] and hv[1] != hv[2] and hv[2] == hv[3] and hv[3] != hv[4]:
        return True
    #card card card pair
    if hv[0] != hv[1] and hv[1] != hv[2] and hv[2] != hv[3] and hv[3] == hv[4]:
        return True
    return False

def isTwoPair(hand):
    hv = getJustValues(hand)
    hv.sort()
    #pair pair card
    if hv[0] == hv[1] and hv[1] != hv[2] and hv[2] == hv[3] and hv[3] != hv[4]:
        return True
    #pair card pair
    if hv[0] == hv[1] and hv[1] != hv[2] and hv[2] != hv[3] and hv[3] == hv[4]:    
        return True
    #card pair pair
    if hv[0] != hv[1] and hv[1] == hv[2] and hv[2] != hv[3] and hv[3] == hv[4]:
        return True
    return False

def isThree(hand):
    hv = getJustValues(hand)
    hv.sort()
    #three card card
    if hv[0] == hv[1] == hv[2] and hv[2] != hv[3] and hv[3] != hv[4]:
        return True
    #card three card
    if hv[0] != hv[1] and hv[1] == hv[2] == hv[3] and hv[3] != hv[4]:
        return True
    #card card three
    if hv[0] != hv[1] and hv[1] != hv[2] and hv[2] == hv[3] == hv[4]:
        return True
    return False


def isFour(hand):
    hv = getJustValues(hand)
    hv.sort()
    #four card
    if hv[0] == hv[1] == hv[2] == hv[3] and hv[3] != hv[4]:
        return True
    #card four
    if hv[0] != hv[1] and hv[1] == hv[2] == hv[3] == hv[4]:
        return True
    return False

def isFullHouse(hand):
    hv = getJustValues(hand)
    hv.sort()
    #three pair
    if hv[0] == hv[1] == hv[2] and hv[2] != hv[3] and hv[3] == hv[4]:
        return True
    if hv[0] == hv[1] and hv[1] != hv[2] and hv[2] == hv[3] == hv[4]:
        return True
    return False


def isStraight(hand):
    hv = getJustValues(hand)
    print(hv)
    hv.sort()
    if hv[0] == hv[1]-1 == hv[2]-2 == hv[3]-3 == hv[4]-4:
        return True
    return False

def isFlush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return True
    return False
