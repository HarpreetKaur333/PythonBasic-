# Programming Exercise 12-1

def main():
 # Local variable
 number = 0

 # Get number as input from the user.
 number = int(input('How many numbers to display? '))

 # Display the numbers.
 print_num(number)

# The print_num function is a a recursive function
# that accepts an integer argument, n , and prints
# the numbers 1 up through n.
def print_num(n):
    if n > 1:
        print_num(n - 1)
    print (n, sep=' ')

# Call the main function.
main()

