# Programming Exercise 12-7

# Global constants for minimum and maximum exponent values
MIN = 1
MAX = 100

def main():
    # Local variables
    num = 0.0
    exp = 0
    
    # Get the number as input from the user.
    num = float(input('Enter a number: '))
    
    # Get the exponent as input from the user.
    while exp < MIN or exp > MAX:
        exp = int(input('Enter a positive whole number between ' \
                        + str(MIN) + ' and ' + str(MAX) + ': '))
        
    # Call the power function and display the result.
    print(num, 'raised to the power of', exp, 'is', \
          format(power(num, exp), ',.2f'))

# The power function uses recursion to raise a number to a power.
# The function accepts two arguments: the number to be raised and
# the exponent.
# The function assumes that the exponent is a nonnegative integer.
def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

# Call the main function.
main()


