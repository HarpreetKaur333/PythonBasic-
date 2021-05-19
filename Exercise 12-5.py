# Programming Exercise 12-5

def main():
    # Initialize a list with values 1 - 10.
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the list.
    print('List of numbers:\n', number_list, sep='')

    # Call the sum_list function and display the
    # sum of all the numbers in the list.
    print('Sum of all the numbers in the list:', \
          sum_list(number_list))

# The sum_list function accepts a list of numbers as an argument.
# The function recursively calculates the sum of all the
# numbers in the list and returns the value.
def sum_list(numlist):
    n  = len(numlist)
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[n-1] + sum_list(numlist[0:n-1])

# Call the main function.
main()

