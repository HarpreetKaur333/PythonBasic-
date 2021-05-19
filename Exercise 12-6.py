# Programming Exercise 12-6

def main():
 # Local variable
 num = 0

 # Get number as input from the user.
 while num <= 0:
     num = int(input('Enter a positive whole number: '))

 # Call the sum_num function and display the sum.
 print('The sum of 1 -', num, 'is', format(sum_nums(num), ','))

# The sum_nums function accepts an integer argument and returns
# the sum of all the integers from 1 up to the number passed as
# an argument.
def sum_nums(n):
    if n == 0:
        return n
    else:
        return n + sum_nums(n-1)

# Call the main function.
main()

