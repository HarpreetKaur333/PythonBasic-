def performOperationOnList():
    numberlist = [] # create empty list
    while True:
        print('P - Print numbers')
        print('A - Add a number')
        print('M - Display mean of the numbers')
        print('S - Display the smallest number')
        print('L - Display the largest number')
        print('F - Find entered number count in list')
        print('Q - Quit')
        userinput = input("Enter your choice:").strip().lower() # ask user to enter choice

        if userinput not in ['p', 'a', 'm', 's', 'l', 'q', 'f']: # check for entered value by use is from choice provided
            print('Unknown selection, please try again')
        else:
            if userinput == 'p': # use input for print list
                if len(numberlist) == 0:
                    print('[] - the list is empty')
                else:
                    strlist = '[ '
                    for number in numberlist:
                        strlist += str(number)+" "
                    strlist += ']'
                    print('Number list => ',strlist)

            elif userinput == 'a': # user input for added integer to list
                while True:
                    try:
                        userinputforInterger = int(input("Please enter integer to add to the list:"))
                        numberlist.append(userinputforInterger)
                        break
                    except ValueError:
                        print("Please enter interger only")

            elif userinput == 'm': # user input to show average of number in list
                if len(numberlist) == 0:
                    print('Unable to calculate the mean - no data')
                else:
                    average = sum(numberlist) / len(numberlist)
                    print('Average => ', average)

            elif userinput == 's': # user input to show smallest number from list
                if len(numberlist) == 0:
                    print('Unable to determine the smallest number - list is empty')
                else:
                    print("The smallest number is ", min(numberlist))

            elif userinput == 'l': # user input to show largest number from list
                if len(numberlist) == 0:
                    print('Unable to determine the largest number - list is empty')
                else:
                    print("The largest number is ", max(numberlist))

            elif userinput == 'f': # find a entered number count in list
                while True:
                    try:
                        userinputforInterger = int(input("Please enter integer to find in list:"))
                        givennumbercount = numberlist.count(userinputforInterger)
                        if givennumbercount > 0:
                            print("Entered number found ", givennumbercount, ' of times')
                        break
                    except ValueError:
                        print("Please enter interger only")

            elif userinput == 'q': # user want to exit from program
                print('Goodbye')
                exit()

if _name_ == '_main_':
    performOperationOnList()