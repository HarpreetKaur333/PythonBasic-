# Programming Exercise 12-8

def main():
    # Test value 1
    num1 = ackermann(0, 3)
    print(num1)

    # Test value 2
    num2 = ackermann(2, 0)
    print(num2)

    # Test value 3
    num3 = ackermann(2, 3)
    print(num3)
    
# Ackermann’s Function is a recursive mathematical algorithm
# that can be used to test how well a system optimizes its
# performance of recursion.
def ackermann(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Call the main function.
main()

