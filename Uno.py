import random

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
    playerCards = Player1(allCards, amountCards)

    while True: 
        player1 = input("Throw in a card: ")
        # player2 = input("Throw in a card: ")
        if player1 in playerCards:
            playerCards = removeCard(playerCards, allCards, player1)
            print(playerCards)
        # if player2 in playerCards:
        #     playerCards = removeCard(playerCards, allCards, player2)
        #     print(playerCards)

def removeCard(playerCards, allCards, player1):
    if player1 in playerCards:
        playerCards.remove(player1)
        if player1 in allCards:
            allCards.remove(player1)
    return playerCards
    # if player2 in playerCards:
    #     playerCards.remove(player2)
    #     if player2 in allCards:
    #         allCards.remove(player2)
    # return playerCards

def specialCard(player1, allCards):
    if player1 == "redPlus2":
        redPlus(allCards)
    elif player1 == "yellowPlus2":
        yellowPlus(allCards)
    elif player1 == "greenPlus2":
        greenPlus(allCards)
    elif player1 == "bluePlus2":
        bluePlus(allCards)
    elif player1 == "plus4cards":
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
    picker = random.sample(allCards, amountCards)
    print("Player1 your cards are", picker)
    return picker


# def computer(allCards, amountCards):
#     picker1 = random.sample(allCards, amountCards)
#     print("Computer's cards are", picker1)
#     return picker1


def main():
    playUno()


if __name__ == "__main__":
    main()
# not finished yet
