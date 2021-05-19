# Programming Exercise 12-2

def main():
    # Local variables
    num1 = 0
    num2 = 0

    # Get the first positive nonzero integer from the
    # user.
    while num1 <= 0:
        num1 = int(input('Enter the first number: '))

    # Get the second positive nonzero integer from the
    # user.
    while num2 <= 0:
        num2 = int(input('Enter the second number: '))
        
    # Call the multipy function, and display the product.
    print(num1, 'times', num2, 'is', multiply(num1, num2))

# The multiply function is a recursive function that
# accepts two arguments into the parameters x and y,
# and returns the value of x times y.
# The function assumes that x and y will always hold
# positive nonzero integers.
def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + multiply(x, y - 1)

# Call the main function.
main()

