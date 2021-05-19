# Assignment 2
# Harpreet kaur ,Harman

def main():
    array_input = []
    rows = int(input('Please enter No of Rows: '))
    columns = int(input('Please enter No of columns : '))
    myFunction(rows, columns, array_input)


# Question 1 Function
def myFunction(rows, columns, array):

    for row in array:
        row[0].append(1)
        row[1].append(0)
        print(array)
    # character = '1'
    # character1 = '0'
    # for row in range(5):
    #
    #     # Each row has fewer columns.
    #     for col in range(4, row, -1):
    #         print(character, end='')
    #
    #     # Go to the next row.
    #     print()


main()
