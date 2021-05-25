# Assignment 2
# Harpreet kaur ,Harman

# Global constants
ROWS = 5  # The number of rows
COLS = 4  # The number of columns


def main():
    # array_input = []
    # rows = int(input('Please enter No of Rows: '))
    # columns = int(input('Please enter No of columns : '))
    # myFunction(rows, columns, array_input)

    array_list = [[1, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 0]
                  [1, 0, 1, 1]
                  [1, 1, 1, 1]]
    display_array_list(array_list)


# Question 1 Function
def display_array_list(array_list):
    for r in range(ROWS):
        for c in range(COLS):
            print(array_list[r][c], end=' ')
        print()
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
