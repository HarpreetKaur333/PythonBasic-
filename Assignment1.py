import sys
import statistics

lst = []

num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
choice = ''
while choice != '0':
    choice = input(""""
        P.Print Numbers
        A.Add Numbers.
        M.Display menu of the Numbers
        S.Display Smallest Number
        L.Display Largest Number
        Q.Exit
        """"")
    if choice == 'P' or choice == 'p':
        print("all Elements of list :", lst)

    elif choice == 'A' or choice == 'a':
        print("Sum of elements in given list is :", sum(lst))
    elif choice == 'M' or choice == 'm':
        print("Mean in given list is :", statistics.mean(lst))
    elif choice == 'S' or choice == 's':
        print("Smallest of elements in given list is :", min(lst))
    elif choice == 'L' or choice == 'l':
        print("Smallest of elements in given list is :", max(lst))
    elif choice == 'Q' or choice == 'q':
        sys.exit()
    else:
        print("Invalid choice ")
