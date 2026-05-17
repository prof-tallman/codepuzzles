# General references:
#  -> https://en.wikipedia.org/wiki/Sudoku
#  -> Looping worksheet from CSC-104


def print_puzzle(puzzle: list[str]) -> None:
    """ Prints a Sudoku puzzle element-by-element with minor spacing. """

    for row in puzzle:
        print(row)


# Thanks to Toby Speight for help with Python strings:
# "In Python, how do I determine whether a string contains a particular character?"
# https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters
# Learned to use the "in" operator to test if a string contains something

def check_sudoku(group: list[str]) -> bool:
    """ Verifies that a Sudoku group contains every digit 1-9 exactly once. """

    if len(group) != 9:
        return False
    
    for digit in "123456789":
        if digit not in group:
            return False
        
    return True


# Couldn't remember exactly how to do list comprehension
# "Examples of list comprehension in python"
# https://www.w3schools.com/python/python_lists_comprehension.asp
# Learned the syntax to translate a for loop to list comprehension

def check_sudoku_row(puzzle: list[str], row: int) -> bool:
    """ Verifies that a Sudoku row contains every digit 1-9 exactly once. """

    if len(puzzle) != 9:
        print(f"Puzzles must contain 9 rows")
        exit()

    elif row < 1 or row > 9:
        print(f"Row numbers must be between [1,9]; {row} is invalid")
        exit()

    else:
        row_idx = row - 1
        group = [puzzle[row_idx][i] for i in range(9)]
        return check_sudoku(group)


def check_sudoku_col(puzzle: list[str], col: int) -> bool:
    """ Verifies that a Sudoku column contains every digit 1-9 exactly once. """

    if any(len(row) != 9 for row in puzzle):
        print(f"Puzzles must contain 9 columns")
        exit()

    elif col < 1 or col > 9:
        print(f"Column numbers must be between [1,9]; {col} is invalid")
        exit()

    else:
        col_idx = col - 1
        group = [puzzle[i][col_idx] for i in range(9)]
        return check_sudoku(group)


# Had trouble putting each of the blocks together
# Talked to Prof. Tallman during office hours
# I learned to use the (x,y) indices of each location in the block and that
# we could ignore the 3x3 structure and just make a single list.

def check_sudoku_block(puzzle: list[str], block: int) -> bool:
    """
    Checks that a Sudoku block contains every digit 1-9 exactly once. The
    blocks are identified by reverse telephone keypad numbering:
      _1_|_2_|_3_
      _4_|_5_|_6_
      _7_|_8_|_9_
    """
    
    # The puzzle object is a 2D 9x9 indexable data structure. This hardcoded
    # list maps from the block indices to 9x9 target indices.
    block_mapping = [
        [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)], # upper-left
        [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)], # upper-middle
        [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)], # upper-right
        [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)], # middle-left
        [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)], # center
        [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)], # middle-right
        [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)], # lower-left
        [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)], # lower-middle
        [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)], # lower-right
    ]

    if len(puzzle) != 9:
        print(f"Puzzles must contain 9 rows")
        exit()

    elif block < 1 or block > 9:
        print(f"Block numbers must be between [1,9]; {block} is invalid")
        exit()

    block_idx = block - 1
    group = [puzzle[i][j] for (i, j) in block_mapping[block_idx]]
    return check_sudoku(group)   


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

    for row_num in range(1, 10):
        valid = check_sudoku_row(my_puzzle, row_num)
        if valid:
            print(f"Sudoku row #{row_num}: good")
        else:
            print(f"Sudoku row #{row_num}: INVALID")

    for col_num in range(1, 10):
        valid = check_sudoku_col(my_puzzle, col_num)
        if valid:
            print(f"Sudoku column #{col_num}: good")
        else:
            print(f"Sudoku column #{col_num}: INVALID")

    for block_num in range(1, 10):
        valid = check_sudoku_block(my_puzzle, block_num)
        if valid:
            print(f"Sudoku group #{block_num}: good")
        else:
            print(f"Sudoku group #{block_num}: INVALID")

