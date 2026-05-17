# Sudoku Solution Validator

Sudoku is a logic puzzle played on a 9×9 grid. The puzzle is divided into rows, columns, and nine 3×3 blocks. A completed Sudoku puzzle is considered valid if every row, every column, and every 3×3 block contains the digits 1–9 exactly once.

This project focuses on validating whether a completed Sudoku solution is correct. The program does **not** need to solve Sudoku puzzles. Instead, it should analyze an already-completed puzzle and determine whether the solution follows the Sudoku rules.

The project is designed to reinforce indexing, loops, functions, strings, arrays/vectors, file parsing, error checking, and modular program design.

## Rankings

These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:
   Write a program that checks whether individual Sudoku rows are valid.

   * Hardcode a completed Sudoku puzzle directly in the source code.
   * Represent the puzzle as a collection of strings or arrays.
   * Write a function that checks whether a single row contains every digit 1–9 exactly once.
   * Print whether each row is valid.

   ```
   user@computer:~$ ./sudoku

   123456789
   456789123
   789123456
   234567891
   567891234
   891234567
   345678912
   678912345
   912345678

   Sudoku row #1: good
   Sudoku row #2: good
   Sudoku row #3: good
   Sudoku row #4: good
   Sudoku row #5: good
   Sudoku row #6: good
   Sudoku row #7: good
   Sudoku row #8: good
   Sudoku row #9: good
   ```

2. ***Script Kiddie***:
   Expand the validator so that it checks rows, columns, and 3×3 blocks.

   * Create separate helper functions for rows, columns, and blocks
   * Detect invalid row/column/block numbers and terminate gracefully.
   * Use loops and indexing instead of hardcoding checks.

   ```
   user@computer:~$ ./sudoku

   123456789
   456789123
   789123456
   234567891
   567891234
   891234567
   345678912
   678912345
   912345678

   Sudoku row #1: good
   Sudoku row #2: good
   ...
   Sudoku row #8: good
   Sudoku row #9: good

   Sudoku column #1: good
   Sudoku column #2: good
   ...
   Sudoku column #8: good
   Sudoku column #9: good

   Sudoku block #1: good
   Sudoku block #2: good
   ...
   Sudoku block #8: good
   Sudoku block #9: good
   ```

3. ***Professional***:
   Refactor the validator to improve readability, maintainability, and error reporting.

   * Create a function that validates the entire puzzle.
   * Use exceptions or structured error handling where appropriate.
   * Detect malformed puzzle data and explain the problem clearly.
   * Use key-value dictionaries to store detailed error information.
   * Improve the puzzle display formatting.
   * Continue using hardcoded puzzles

   ```
   user@computer:~$ ./sudoku

   -=| Sudoku Check |=-

   -------------
   |123|456|789|
   |456|789|123|
   |789|123|456|
   |---+---+---|
   |234|567|891|
   |567|891|234|
   |891|234|567|
   |---+---+---|
   |345|678|912|
   |678|912|345|
   |912|345|678|
   -------------

   Congratulations, the Sudoku solution is correct
   ```

4. ***1337 H@cker***:
   Convert the validator into a professional command-line utility.

   * Read Sudoku puzzles from a text file.
   * Accept the puzzle filename from the command line.
   * Add an optional command-line flag to choose whether to print the puzzle.
   * Validate the puzzle file format before processing.
   * Handle malformed files, missing files, and invalid arguments gracefully.
   * Document the required file format in the command-line help output.
   * Generate clear error messages that identify the exact row and/or column where formatting problems occur.

   ```
   user@computer:~$ ./sudoku puzzle.txt --print

   -=| Sudoku Check |=-

   -------------
   |123|456|789|
   |456|789|123|
   |789|123|456|
   |---+---+---|
   |234|567|891|
   |567|891|234|
   |891|234|567|
   |---+---+---|
   |345|678|912|
   |678|912|345|
   |912|345|678|
   -------------

   Congratulations, the Sudoku solution is correct
   ```

   ```
   user@computer:~$ ./sudoku bad_puzzle.txt

   Row 1, column 5: Invalid digit 'x'
   Row 4: Row does not contain exactly 9 digits

   Error: Puzzle file is invalid
   ```

   ```
   user@computer:~$ ./sudoku missing_file.txt

   Error: File 'missing_file.txt' does not exist
   ```

5. ***BONUS***:
   Add one or more advanced features:

   * Highlight invalid rows/columns visually
   * Export formatted puzzle reports to a file
   * Benchmark multiple validation approaches
   * Create a Sudoku puzzle solver

## AI Restrictions

Students are allowed to use AI LLMs such as ChatGPT to lookup basic programming concepts, syntax, libraries, or examples within the programming language. For example, somebody might ask how command-line arguments work in C++, how exceptions are typically handled, or how to read a text file line-by-line.

However, students are prohibited from providing the AI with information about the Sudoku assignment itself. Students may not ask the AI to generate Sudoku validation algorithms, helper functions, or project-specific code. If the AI guesses the project context and begins generating solution code, students should ignore that portion of the response.

Students may use AI as a learning and documentation tool, but not as a substitute for designing and writing the project themselves.

All external resources, including AI prompts, tutorials, StackOverflow discussions, office-hours help, classmates, and documentation references must be cited in comments near the relevant code.

## Constraints

* The puzzle must represent a standard 9×9 Sudoku board.
* The validator only needs to verify completed Sudoku solutions.
* The program does not need to solve incomplete puzzles.
* The program should be written primarily by the student.

## Resources

Students may find the following topics useful:

* Arrays and vectors
* String indexing
* File input/output
* Exception handling
* Command-line argument parsing
* Dictionaries/maps/structures
* Nested loops
* Helper functions and decomposition