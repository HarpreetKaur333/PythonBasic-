# Programming Exercise 12-3

def main():
 # Local variable
 number = 0

 # Get number of lines as input from the user.
 number = int(input('How many lines to display? '))

 # Display the lines.
 print_lines(number)

# The print_lines function is a recursive function that
# accepts an integer argument, n. The function displays
# n lines of asterisks on the screen, with the first
# line showing 1 asterisk, the second line showing 2
# asterisks, up to the nth line which shows n asterisks.
def print_lines(n):
    if n > 1:
        print_lines(n - 1)
    for i in range(n):
        print('*', end='')
    print()

# Call the main function.
main()
