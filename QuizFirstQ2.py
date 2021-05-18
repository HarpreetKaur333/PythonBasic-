import sys
import statistics
import random


def gen():
    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    answerF = number1 * number2
    print("What is", number1, "x", number2, "?")
    return answerF


def main():
    print("Welcome to the multiplication game.")
    print("How well do you know multiplication tables?")
    guess = 0

    answer = gen()
    while guess != answer:
        guess = int(input("Answer: "))
        if guess != answer:
            print("No, try again")
        else:
            print("very good!")


main()
