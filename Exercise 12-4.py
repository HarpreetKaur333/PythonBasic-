# Programming Exercise 12-4

def main():
    # Initialize a list with values 1 - 10.
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the list.
    print('List of numbers:\n', number_list, sep='')

    # Call the find_largest function and display the
    # largest number in the list.
    print('Largest number in the list: ', find_largest(number_list))

# The find_largest function accepts a list as an argument
# and returns the largest value in the list.
# The function uses recursion to find the largest item.
def find_largest(numlist):
    n  = len(numlist)
    if n == 1:
        return numlist[0]
    else:
        temp = find_largest(numlist[0:n-1])
        if numlist[n-1] > temp:
            return numlist[n-1]
        else:
            return temp

# Call the main function.
main()

