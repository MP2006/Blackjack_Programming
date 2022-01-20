from art import logo

import random


def newCardDeck():
    initialCard = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    cardType = ["♦", "♥", "♣", "♠"]
    cardDeck = []
    for i in initialCard:
        for j in cardType:
            card = i + " " + j
            cardDeck.append(card)

    return cardDeck


def randomCard(cardDeck):
    selectCard = random.choice(cardDeck)
    cardDeck.remove(selectCard)

    return selectCard


def startingCard(cardDeck):
    cardList = []
    for i in range(2):
        cardList.append(randomCard(cardDeck))

    return cardList


def detectValue(card):
    value = card[0]
    listChar = ["J", "K", "Q"]
    if value in listChar:
        value = 10
    elif value == "A":
        value = 11
    elif value == "1":
        value = 10
    else:
        value = int(value)

    return value


def calculateScore(playerCards):
    score = 0
    for i in range(len(playerCards)):
        tempScore = detectValue(playerCards[i])
        score += tempScore

    return score


# a = userWin, b = computer Win
def blackjackCheck(userScore, computerScore, computerCard, userCard, winList):
    if userScore == 21 and computerScore == 21:
        print("_____________________________________________________")
        print("\nIt's a draw. Both players have Blackjack!")
        print("\nYour final cards are:")
        for i in range(len(userCard)):
            print(userCard[i], end="  ")
        print("\n\nComputer's final cards are:")
        for j in range(len(computerCard)):
            print(computerCard[j], end="  ")
        print("\n_____________________________________________________")
        return True
    elif userScore == 21:
        print("_____________________________________________________")
        print("\nYou get Blackjack! You win!")
        winList.append("a")
        print("\nYour final cards are:")
        for i in range(len(userCard)):
            print(userCard[i], end="  ")
        print("\n_____________________________________________________")
        return True
    elif computerScore == 21:
        print("_____________________________________________________")
        print("\nComputer gets Blackjack! Computer wins!")
        winList.append("b")
        print("\n\nComputer's final cards are:")
        for j in range(len(computerCard)):
            print(computerCard[j], end="  ")
        print("\n_____________________________________________________")
        return True
    else:
        return False


def printCard(userCard, computerCard, youScore):
    print("_____________________________________________________")
    print("\nYour current cards are:")
    for i in range(len(userCard)):
        print(userCard[i], end="  ")
    print(f"\n=> Your current score is {youScore}")
    print(f"\nComputer's first card: \n{computerCard[0]}")


def computerPlay(computerScore, computerCard, cardDeck):
    while computerScore < 17:
        computerCard.append(randomCard(cardDeck))
        computerScore = calculateScore(computerCard)
    return computerScore


# a = userWin, b = computer Win
def result(computerCard, userCard, computerScore, userScore, winList):
    print("_____________________________________________________")
    print(f"\nYour final cards are (value {userScore}):")
    for i in range(len(userCard)):
        print(userCard[i], end="  ")
    print(f"\n\nComputer's final cards are (value {computerScore}):")
    for j in range(len(computerCard)):
        print(computerCard[j], end="  ")
    print("\n")
    if computerScore > 21 and userScore > 21:
        print("Bust! Both players lost.")
    elif computerScore > 21:
        print("Computer busts. You win!")
        winList.append("a")
    elif userScore > 21:
        print("You bust. Computer wins!")
        winList.append("b")
    elif computerScore > userScore:
        print(f"Computer has a higher score. {computerScore} vs {userScore}, computer wins!")
        winList.append("b")
    elif userScore > computerScore:
        print(f"You have a higher score. {userScore} vs {computerScore}, you win!")
        winList.append("a")
    elif userScore == computerScore:
        print("It's a tie!")
    print("_____________________________________________________")


def checkForA(playerCards):
    score = calculateScore(playerCards)
    for i in range(len(playerCards)):
        card = playerCards[i]
        if card[0] == "A":
            score = score - 10
            if score < 21:
                break
    return score


# a = userWin, b = computer Win
def winCounter(winList):
    a = 0
    b = 0
    for i in winList:
        if i == "a":
            a += 1
        elif i == "b":
            b += 1
    print(f'''
You | Computer
-------------
{a}   |  {b}
    ''')


def main():
    choice = "y"
    winList = []
    while choice == "y":
        print(logo)
        print("Welcome to the game of Blackjack!")
        deck = newCardDeck()
        random.shuffle(deck)
        userCards = startingCard(deck)
        computerCards = startingCard(deck)
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        printCard(userCards, computerCards, userScore)
        check = blackjackCheck(userScore, computerScore, computerCards, userCards, winList)
        if check:
            winCounter(winList)
            choice = input("\nWould you like to play another game? (y or n): ").lower()
        else:
            option = "y"
            computerScore = computerPlay(computerScore, computerCards, deck)
            if computerScore > 21:
                computerScore = checkForA(computerCards)
                if computerScore < 21:
                    computerPlay(computerScore, computerCards, deck)
                    computerScore = checkForA(computerCards)
            while option == "y":
                option = input("\nType 'y' to pick another card, type 'n' to pass: ").lower()
                if option == "y":
                    userCards.append(randomCard(deck))
                    userScore = calculateScore(userCards)
                    if userScore > 21:
                        userScore = checkForA(userCards)
                        printCard(userCards, computerCards, userScore)
                        if userScore > 21:
                            option = "n"
                            result(computerCards, userCards, computerScore, userScore, winList)
                            winCounter(winList)
                            choice = input("\nWould you like to play another game? (y or n): ").lower()
                    else:
                        printCard(userCards, computerCards, userScore)
                else:
                    result(computerCards, userCards, computerScore, userScore, winList)
                    winCounter(winList)
                    choice = input("\nWould you like to play another game? (y or n): ").lower()

        print("\nThank you for playing Blackjack!")


main()
