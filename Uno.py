import random
#updated if currentCard matches player1 and player2
def playUno():
    redCard = ["red0", "red1", "red2", "red3", "red4", "red5", "red6", "red7", "red8", "red9", "redReverse", "redPlus2"]
    yellowCard = ["yellow0", "yellow1", "yellow2", "yellow3", "yellow4", "yellow5", "yellow6", "yellow7", "yellow8",
                  "yellow9", "yellowReverse", "yellowPlus2"]
    greenCard = ["green0", "green1", "green2", "green3", "green4", "green5", "green6", "green7", "green8", "green9",
                 "greenReverse", "greenPlus2"]
    blueCard = ["blue0", "blue1", "blue2", "blue3", "blue4", "blue5", "blue6", "blue7", "blue8", "blue9", "blueReverse",
                "bluePlus2"]
    specialCard = ["red, yellow, blue, or green", "plus4cards"]

    allCards = redCard + yellowCard + greenCard + blueCard + specialCard
    amountCards = 7
    player1Cards = Player1(allCards, amountCards)
    player2Cards = Player2(allCards, amountCards)
    currentCard = random.choice(allCards)
    
    while True:
        if currentCard.startswith("red"):
            currentColor = "red"
        elif currentCard.startswith("yellow"):
            currentColor = "yellow"
        elif currentCard.startswith("green"):
            currentColor = "green"
        elif currentCard.startswith("blue"):
            currentColor = "blue"
   
        print("Current Card:", currentCard)
    
        player1 = input("Player 1, throw in a card: ")
        if player1.startswith("red"):
            player1Color = "red"
        elif player1.startswith("yellow"):
            player1Color = "yellow"
        elif player1.startswith("green"):
            player1Color = "green"
        elif player1.startswith("blue"):
            player1Color = "blue"

        
        if player1Color == currentColor or player1.startswith("plus4cards"):
            print('Player 1: True')
        else:
            print('Player 1: False')
            return
        
        if player1 in player1Cards:
            player1Cards = removeCard(player1Cards, allCards, player1)
            print("Player 1 your cards are:", player1Cards)
        else:
            print("Card not found in Player 1's hand")
        

        print("Current Card:", currentCard)
        
        player2 = input("Player 2, throw in a card: ")
        if player2.startswith("red"):
            player2Color = "red"
        elif player2.startswith("yellow"):
            player2Color = "yellow"
        elif player2.startswith("green"):
            player2Color = "green"
        elif player2.startswith("blue"):
            player2Color = "blue"
        else:
            player2Color = None

        if player2Color == currentColor or player2.startswith("plus4cards"):
            print('Player 2: True')
        else:
            print('Player 2: False')
            return
        
        if player2 in player2Cards:
            player2Cards = removeCard(player2Cards, allCards, player2)
            print("Player 2 your cards are:", player2Cards)
        else:
            print("Card not found in Player 2's hand")
        

def removeCard(playerCards, allCards, cardToRemove):
    if cardToRemove in playerCards:
        playerCards.remove(cardToRemove)
    if cardToRemove in allCards:
        allCards.remove(cardToRemove)
    return playerCards

def specialCard(card, allCards):
    if card == "redPlus2":
        redPlus(allCards)
    elif card == "yellowPlus2":
        yellowPlus(allCards)
    elif card == "greenPlus2":
        greenPlus(allCards)
    elif card == "bluePlus2":
        bluePlus(allCards)
    elif card == "plus4cards":
        plus4(allCards)


def redPlus(allCards):
    red = random.sample(allCards, 2)
    print("Red Plus cards:", red)


def yellowPlus(allCards):
    yellow = random.sample(allCards, 2)
    print("Yellow Plus cards:", yellow)


def greenPlus(allCards):
    green = random.sample(allCards, 2)
    print("Green Plus cards:", green)


def bluePlus(allCards):
    blue = random.sample(allCards, 2)
    print("Blue Plus cards:", blue)


def plus4(allCards):
    special = random.sample(allCards, 4)
    print("Plus 4 cards:", special)


def Player1(allCards, amountCards):
    picker1 = random.sample(allCards, amountCards)
    print("Player 1 your cards are", picker1)
    return picker1

def Player2(allCards, amountCards):
    picker2 = random.sample(allCards, amountCards)
    print("Player 2 your cards are", picker2)
    return picker2


def main():
    playUno()


if __name__ == "__main__":
    main()

