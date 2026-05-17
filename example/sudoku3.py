# General references:
#  -> https://en.wikipedia.org/wiki/Sudoku

def print_puzzle(puzzle: list[str]) -> None:
    """ Prints a Sudoku puzzle in ASCII-art style. """
    print("-------------")
    for row in puzzle[0:3]:
        print(f"|{row[0:3]}|{row[3:6]}|{row[6:9]}|")
    print("|---+---+---|")
    for row in puzzle[3:6]:
        print(f"|{row[0:3]}|{row[3:6]}|{row[6:9]}|")
    print("|---+---+---|")
    for row in puzzle[6:9]:
        print(f"|{row[0:3]}|{row[3:6]}|{row[6:9]}|")
    print("-------------")


# GenAI:
# "In Python, what exception type should be raised for bad function arguments?"
# I learned that TypeError and ValueError are the two most common exceptions
# and the choice depends on whether it's a data type or value (number) error.

def verify_puzzle_dimensions(puzzle: list[str]) -> None:
    """ Raises ValueError if the puzzle dimensions are invalid. """
    if len(puzzle) != 9:
        raise ValueError("Puzzle must contain exactly 9 rows")
    if any(len(row) != 9 for row in puzzle):
        raise ValueError("Each puzzle row must contain exactly 9 digits")


def verify_index(name: str, index: int) -> None:
    """ Raises ValueError if an index is not between 1 and 9. """
    if index < 1 or index > 9:
        raise ValueError(
            f"Value '{name}' must be between 1 and 9;"
            f" {index} is invalid"
        )


def check_sudoku_group(group: list[str]) -> bool:
    """ Checks that a Sudoku group contains every digit 1-9 exactly once. """

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
    """ Checks that a Sudoku row contains every digit 1-9 exactly once. """
    verify_puzzle_dimensions(puzzle)
    verify_index('row', row)
    row_idx = row - 1
    group = [puzzle[row_idx][i] for i in range(9)]
    return check_sudoku_group(group)


def check_sudoku_col(puzzle: list[str], column: int) -> bool:
    """ Checks that a Sudoku column contains every digit 1-9 exactly once. """
    verify_puzzle_dimensions(puzzle)
    verify_index('column', column)
    column_idx = column - 1
    group = [puzzle[i][column_idx] for i in range(9)]
    return check_sudoku_group(group)


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

    verify_puzzle_dimensions(puzzle)
    verify_index('block', block)
    block_idx = block - 1
    group = [puzzle[i][j] for (i, j) in block_mapping[block_idx]]
    return check_sudoku_group(group)


def check_sudoku_puzzle(puzzle: list[str]) -> bool:
    """
    Checks that a 9x9 Sudoku puzzle is 100% valid, containing every digit
    1-9 in every row, every column, and every block.
    """

    # Check every row, column, and block 1-9 for invalid numbers
    for index in range(1, 10):
        if (not check_sudoku_row(puzzle, index) or
            not check_sudoku_col(puzzle, index) or
            not check_sudoku_block(puzzle, index)):
            return False

    # Every row, column, and block passed so the puzzle must be valid
    return True


# Had to use the Dictionary Worksheet from CSC-104

def check_puzzle_format(puzzle: list[str]) -> list[dict]:
    """ Verifies that a puzzle file contains valid Sudoku formatting. """

    errors = []

    if len(puzzle) != 9:
        errors.append({
            "row": len(puzzle) + 1,
            "message": f"Puzzle contains {len(puzzle)} rows instead of 9"
        })

    for row_num, row in enumerate(puzzle):
        if len(row) != 9:
            errors.append({
                "row": row_num + 1,
                "message": "Row does not contain exactly 9 digits"
            })
        for col_num, ch in enumerate(row):
            if ch not in "123456789":
                errors.append({
                    "row": row_num + 1,
                    "column": col_num + 1,
                    "message": f"Invalid digit '{ch}'"
                })

    return errors


def main():

    try:
        print("\n-=| Sudoku Check |=-")

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

        errors = check_puzzle_format(my_puzzle)
        if len(errors) != 0:
            for error in errors:
                location = f"Row {error['row']}"
                if "column" in error:
                    location += f", column {error['column']}"
                print(f"{location}: {error['message']}")
            print("Error: Puzzle file is invalid\n")
        else:
            if check_sudoku_puzzle(my_puzzle):
                print("Congratulations, the Sudoku solution is correct\n")
            else:
                print("Unfortunately, the provided solution is invalid\n")

    except ValueError as error:
        print(f"\nError: {error}\n")


if __name__ == '__main__':
    main()
