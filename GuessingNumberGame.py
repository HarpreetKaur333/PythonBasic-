# generate 100 random number  between 1 and 100
import random


def main():
    randNumber = 0
    userEntered = 0

    randNumber = random.randint(1, 100)

    GuessingFun(randNumber)


def GuessingFun(randNumber):
    userEntered = int(input("enter a number between 1 and 100  "))

    while userEntered > 0:

        if userEntered > randNumber:
            print("you entered too high number.. try again")
            userEntered = int(input("enter a number between 1 and 100   "))

        elif userEntered < randNumber:
            print("you entered too low number ... try again")
            userEntered = int(input("enter a number between 1 and 100   "))
        else:
            print("ur guess is right..! you won")
            return userEntered

            return userEntered


main()
