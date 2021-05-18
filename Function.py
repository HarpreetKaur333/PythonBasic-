import random


# generate 100 random number  between 1 and 100
# count number is even or odd
# def main():
#     first = int(input("Enter first integer: "))
#     second = int(input("Enter second integer: "))
#     Is_evenodd(first, second)
#
#
# def Is_evenodd(first, second):
#     for x in range(20):
#         randNumber = random.randrange(first, second)
#         if randNumber % 2 == 0:
#             print("The random number is even.", randNumber)
#         elif randNumber % 2 != 0:
#             print("The random number is odd.", randNumber)
#
#
# main()

# get the user integer ,then check prime number

def main():
    n = input("Please enter a number:")
    is_prime(n)


def is_prime(x):
    localvar = True
    for i in (2, x):
        while localvar:
            if (x % i) == 0:
                localvar = False
            else:
                localvar = True

    if localvar:
        print("prime")
    else:
        print("not prime")


main()
