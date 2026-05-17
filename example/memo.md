# Technical Investigation Memo

The goal of this project was to verify whether a completed Sudoku puzzle is valid. The code did not need to generate a solution; it accepted a completed puzzle and determined if the solution was valid. A valid Sudoku solution contains the digits 1–9 exactly once in every row, every column, and every 3×3 block.

## 1. Problem Definition

Although the rules of Sudoku are simple, there are several technical challenges involved in implementing a validator correctly. The most important challenge is organizing the puzzle data in memory in a way that makes rows, columns, and blocks easy to examine. The project also requires careful indexing because Python lists start at zero while Sudoku puzzles are usually described using rows and columns numbered 1–9.

Another important challenge is input validation. Since the program will eventually read puzzles from a text file, the code must handle malformed puzzles safely and explain formatting problems clearly to the user.

## 2. Design Hypothesis

My original plan was to represent the Sudoku puzzle as a 9×9 two-dimensional list. This structure makes it easy to access rows and columns using list indexing. However, after experimenting with the design, I decided to represent the puzzle as a list of strings instead. Each string represents one row of the puzzle. For example:

```
puzzle = [
    "123456789",
    "456789123",
    "789123456",
    ...
]
```

This structure still allows indexing using `puzzle[row][column]`, but it also simplifies reading puzzles from text files because each line from the file already corresponds to a row.

My hypothesis was that the best design would use separate helper functions for checking rows, columns, and blocks. Each helper function would extract a “group” of nine digits and then pass that group into a shared validation function.

Also, I noted that performance would not be especially important because Sudoku puzzles are very small.

## 3. Investigation

### Source 1: Office Hours Discussion About Sudoku Blocks

I initially struggled to determine how the 3×3 Sudoku blocks should be represented in code, so I met with Prof. Tallman in office hours. We discussed how the validator did not need to preserve the visual 3×3 structure internally. Instead, each block could simply be converted into a flat list of nine values.

Advantages:

* Simplified the indexing and validation code
* Made the block-checking logic more consistent with row and column checking

Disadvantages:

* Required creating a mapping structure between block numbers and puzzle coordinates
* The hardcoded mapping table takes a little while to read and understand

This discussion influenced the final implementation of the block validation system.

### Source 2: Python List Comprehensions Article

https://www.w3schools.com/python/python_lists_comprehension.asp

I reviewed examples of Python list comprehensions because I could not remember the exact syntax. The article showed how a new list can be generated directly from a loop.

Advantages:

* Compact syntax
* Reduces repeated code

Disadvantages:

* Can become difficult to read when expressions become complicated
* Some beginners may find the syntax unfamiliar

I decided that reducing the code outweighed the complicated syntax.

### Source 3: CSC-104 Dictionary Worksheet

Course worksheet from CSC-104.

I reviewed the dictionary worksheet while designing the puzzle format error checking system. The worksheet explained how dictionaries can store related pieces of information using key-value pairs.

Advantages:

* Groups related information together clearly
* Makes error reporting easier to organize
* The descriptive text keys make error messages easier to understand than using a list.

Disadvantages:

* Requires careful consistency in key names

The assignment required us to use dictionaries for the Professional Level, but I can see how the text keys make it easier to understand the error messages, especially when there are multiple errors for the same file.

### Source 4: GenAI Discussion About Exceptions

The project required using exceptions but we didn't spend too much time covering these in class, so I knew that I would have to research them myself. Claude prompt:

> "In Python, what exception type should be raised for bad function arguments?"

I used GenAI to understand the difference between TypeError and ValueError. The discussion explained that TypeError is usually used when the data type is incorrect, while ValueError is used when the type is correct but the value itself is invalid.

Advantages:
* Helped clarify standard Python error-handling conventions
* Improved the readability and correctness of the program

Disadvantages:
* AI explanations can sometimes be overly broad or inconsistent

The AI provided multiple possible approaches, which required judgment to evaluate. In the end, I decided to raise `ValueError` exceptions when Sudoku row, column, or block numbers fall outside the range 1–9.

## 4. Final Design Decision

The final program stores the Sudoku puzzle as a list of strings. Rows, columns, and blocks are extracted using indexing and list comprehensions.

The design uses several helper functions:

```
_check_sudoku_group()
check_sudoku_row()
check_sudoku_col()
check_sudoku_block()
```

I decided to make the first helper function private because any programmers using my code should access it through the row, column, and block helper functions.

This decomposition reduces duplicated code and makes the program easier to debug.

I decided to use a hardcoded mapping table for the 3×3 blocks rather than calculating the indices mathematically. Although the mathematical solution may be shorter, the hardcoded version is easier to understand.

I also added exception handling and puzzle-format validation so that malformed puzzles generate clear error messages instead of crashing unexpectedly.

## 5. Reflection

The original design worked fairly well, but several implementation details became more important during development.

The biggest challenge was correctly extracting the 3×3 blocks. Initially, I tried to preserve the visual 3×3 structure of the blocks, but this complicated the indexing logic. During office hours, I realized that the validator only needed a flat list of nine values, which simplified the design considerably.

Another important realization was that Python sets greatly simplified the group validation logic. My original solution used many repeated comparisons, which worked but was harder to read and maintain.

If I restarted the project, I would like to add a new feature that would print malformed puzzles with an arrow that shows exactly where the format error occurs; something like this:

```
123|4x6|789
-----^
Error: invalid digit at row 1 column 5
```

My final solution successfully validates Sudoku rows, columns, and blocks and produces clear error messages when errors occur. The code is modular and significantly easier to maintain than my original design.