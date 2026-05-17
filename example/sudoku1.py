# General references:
#  -> https://en.wikipedia.org/wiki/Sudoku
#  -> Looping worksheet from CSC-104

def print_puzzle(puzzle: list[str]) -> None:
    for row in puzzle:
        print(row)


# Thanks to Toby Speight for help with Python strings:
# "In Python, how do I determine whether a string contains a particular character?"
# https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters
# Learned to use the "in" operator to test if a string contains something

def sudoku_check(row: str) -> bool:
    return (
        len(row) == 9
        and "1" in row and "2" in row and "3" in row
        and "4" in row and "5" in row and "6" in row
        and "7" in row and "8" in row and "9" in row
    )


if __name__ == '__main__':

    my_puzzle = [
        "123456789",
        "456789123",
        "789123456",
        "234567891",
        "567891234",
        "891234567",
        "345678912",
        "678912345",
        "912345678"
    ]

    print_puzzle(my_puzzle)

    for x in range(9):
        valid = sudoku_check(my_puzzle[x])
        if valid:
            print(f"Sudoku row #{x+1}: good")
        else:
            print(f"Sudoku row #{x+1}: INVALID")
