# Programming Exercise 5-19

# main function
def main():

    # Local variables to hold user input
    presentValue = 0.0
    interestRate = 0.0
    months = 0
    futureValue = 0.0

    # Get user input for specific values
    presentValue = float(input('Enter the present value ' \
                               'of the account in dollars: '))
    
    interestRate = float(input('Enter the monthly interest ' \
                               'rate as a  percentage: '))
    
    months = int(input('Enter the number of months: '))

    # Get expected future value of the account
    futureValue = getFutureValue(presentValue, interestRate, months)

    print ('The information for your account is:')
    print('Present value: $', format(presentValue, ',.2f'), sep='')
    print('Interest Rate: %', format(interestRate, '.2f'), sep='')
    print('After ', months, \
          ' months, the value of your account will be $', \
          format(futureValue, '.2f'), sep='')

# The getFutureValue function receives the present value, the 
# interest percentage, and the number of months that the money will 
# be in the account, and returns the future value of the account. 
def getFutureValue(P, interest, t):
    # Define local variable
    F = 0.0
    i = interest / 100 # write the percentage as a fraction
    F = P * ((1 + i) **t)
    return F

# Call the main function.
main()


