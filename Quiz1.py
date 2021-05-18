# Quiz1
#  HarpreetKaur , Harman

import sys
import statistics
import random


def main():
    # calling of Question1
    Number1 = int(input("Please enter first number: "))
    Number2 = int(input("Please enter first number: "))
    checkRelation(Number1, Number2)
    print("\n")

    # Calling of Question2
    print("\n")
    print("Welcome to the multiplication game.")
    print("How well do you know multiplication of one digit number ?")
    guess = 0
    answer = gen()

    while guess != answer:
        guess = int(input("Answer: "))
        if guess != answer:
            print("No, try again")
        else:
            print("very good!")
            answer = gen()


# Question 1 Function
def checkRelation(Number1, Number2):
    FactorsFirstNumList = []
    FactorsSecondNumList = []
    sumFirstList = 0
    sumSecondList = 0
    for i in range(1, Number1 - 1):
        if Number1 % i == 0:
            FactorsFirstNumList.append(i)
            sumFirstList = sum(FactorsFirstNumList)

    print("Factors of First Number: ", FactorsFirstNumList)
    print("Sum of all factors of entered Number: ", sumFirstList)

    for j in range(1, Number1 - 1):
        if Number2 % j == 0:
            FactorsSecondNumList.append(j)
            sumSecondList = sum(FactorsSecondNumList)

    print("Factors Of Second Number: ", FactorsSecondNumList)
    print("sum of all factors of entered Number: ", sumSecondList)

    if sumFirstList == sumSecondList:
        print("Both Numbers has Relation")
    else:
        print("No Relation")


# Question 2 Function
def gen():
    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    answerF = number1 * number2
    print("What is", number1, "x", number2, "?")
    return answerF


main()
