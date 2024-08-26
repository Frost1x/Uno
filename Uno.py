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
    playerCards = player(allCards, amountCards)

    while True:
        userInput = input("Throw in a card: ")
        if userInput in playerCards:
            playerCards = removeCard(playerCards, allCards, userInput)
            print(playerCards)

def removeCard(playerCards, allCards, userInput):
    if userInput in playerCards:
        playerCards.remove(userInput)
        if userInput in allCards:
            allCards.remove(userInput)
    return playerCards

def specialCard(userInput, allCards):
    if userInput == "redPlus2":
        redPlus(allCards)
    elif userInput == "yellowPlus2":
        yellowPlus(allCards)
    elif userInput == "greenPlus2":
        greenPlus(allCards)
    elif userInput == "bluePlus2":
        bluePlus(allCards)
    elif userInput == "plus4cards":
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


def player(allCards, amountCards):
    picker = random.sample(allCards, amountCards)
    print("Your cards are", picker)
    return picker


def computer(allCards, amountCards):
    picker1 = random.sample(allCards, amountCards)
    print("Computer's cards are", picker1)
    return picker1


def main():
    playUno()


if __name__ == "__main__":
    main()
# not finished yet
