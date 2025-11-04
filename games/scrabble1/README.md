# Scrabble Word Score Calculator #
Build a program that scores a Scrabble play based on the word placed and the position on the board.

Scrabble is a board game where players place tiles to form words and earn points. Each letter tile has a different point value, and certain board squares provide multipliers (e.g., double letter score, triple word score). A valid placement must fit on the board, use only available tiles, and spell an approved word.

Your program will:
- Check whether a word fits on the standard 15×15 Scrabble board
- Validate the word using a dictionary file
- Verify tile availability (including wildcards)
- Calculate the correct score, applying board multipliers

**Note:** Do not attempt to validate real Scrabble gameplay rules such as cross-words or turn legality. This assignment focuses strictly on scoring a single placed word, top-to-bottom or left-to-right.

## Rankings ##
These stages are friendly suggestions. Skilled students may implement in any order or improve upon them.

1. 🧸 ***AI Does My HW***:
   Write a function that determines whether a word fits on the Scrabble board.
   - Word is given as a string (assume uppercase `A–Z` and `_` for wildcard)
   - User provides starting position as `(row, col)` where both range 1–15
   - Direction is `'A'` for across or `'D'` for down
   - Assume the word itself is valid (for now)
   - Return True if the word fits inside the board; otherwise False
   Print a few hard-coded test cases.
   ```
   $ python scrabble.py
   Testing board fit...
   WORD at (1,1) A → True
   PYTHON at (10,12) A → False
   GAME at (12,1) D → True
   ```

2. 👾 ***Script Kiddie***:
   Add logic to verify whether a word is legal in Scrabble.
   Implement three helper functions:
   - Load dictionary from words_alpha.txt into a fast data structure (e.g., set)
   - Verify that the word is in the official word list (ignoring the wildard tile `'_'`)
   - Tile availability check
     - Use a hard-coded tile-count data structure (e.g., `{ 'E':12, 'A':9, ..., 'Z':1, '_':2 }`)
     - `'_'` represents a blank tile and counts as 0 points later
     - Reject the word if it requires more letters than exist
   Print test results after loading the dictionary.
   ```
   user@computer:~$ python scrabble.py
   Validating words...
   HELLO → tiles ok, in dictionary
   ZZZ → tiles exhausted → invalid
   QXZ → not found in dictionary → invalid
   ```

3. 🧑‍💼 ***Professional***:
   Compute the base Scrabble score (no board bonuses yet).
   - Write a function that computes the score for a word
   - Use hard-coded tile scores (A=1, B=3, ..., Z=10, _ = 0)
   - Return an integer total
   Add a CLI loop to type words and show score
   - Exit cleanly on `'quit'`, `'exit'`, or `<CTRL>+C`
   ```
   user@computer:~$ python scrabble.py
   Enter word: HELLO
   Base score: 8
   Enter word: QI
   Base score: 11
   Enter word: quit
   ```

4. 🧠 ***1337 H@cker***:
   Implement full Scrabble scoring.
   - Use a hard-coded 15×15 board with the standard bonus squares (e.g., double-letter, triple-word, etc)
   - Public entry point: score_play(word, row, col, direction)
   - Steps:
     - Validate the word (fits, in dictionary, tiles ok)
     - Apply letter bonuses (DL/TL)
     - Sum base score
     - Apply word bonuses (DW/TW)
     - Return integer score
   - Raise exceptions for invalid plays
   Interactive mode accepts input words, xy-location, and directional orientation.
   ```
   $ python scrabble.py
   Enter play: ZEBRA 1 2 A
     --> Score: 32  (double word bonus!)
   Enter play: Z_EBRA 7 8 D
     --> Score: 14  (blank tile!)
   Enter play: ZABRE 2 3 D
     --> Error: invalid word
   Enter play: ZEBRA 14 3 A
    --> Error: word goes off board
   Enter play: quit
   ```

5. 🎁 ***BONUS***:
   Add any/all of the following:
   - Display the board with placed letters for visualization
   - Optional `--dictionary FILE` and `--board FILE` flags

## AI Restrictions
Students may use AI to look up things like: string parsing, file reading, dictionary/set usage, command-line argument handling, and error handling patterns.

Students may not:
- Paste this assignment description into any AI model
- Ask the AI to solve the assignment or write the program
- Provide the AI any project code or output

In summary, AI may be used as a lookup tool, not a code-writing tool.

## Constraints ##
Projects must comply with the following rules:
- Standard 15×15 Scrabble board
- Coordinates are 1-indexed (1–15)
- `'_'` stands for a blank tile, counts as any letter, and scores 0
- Raise an exception for invalid plays (your game loop should catch these exceptions and handle them gracefully)
- Do not validate full Scrabble gameplay (cross-checking, rack limits, etc.)

## Resources ##
The Scrabble Word Score Calculator will need a list of approved words that it can use to verify user input. The official Scrabble dictionary is available to members of the North American Scrabble Players Association (NASPA) as a text file; however, it is not released to the public. Therefore, this project will use a publically available dictionary obtained from DWYL's github repository. DWYL posted a text file containing 479k English words based on a file from Info Chimps. **Warning**: there are "words" in this file that are obviously not real words... but it's a reasonable dictionary in the public domain.
- [words_alpha.txt](words_alpha.txt)
