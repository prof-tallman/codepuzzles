# Scrabble Word Score Calculator #
Calculate the score of a word on the Scrabble board. Users will provide a word and a location. The program should output the score.

![Picture of Scrabble Board from Engineering Lab](scrabble.jpg)

## Constraints ##
The code should be implemented as a publically available function. Wrap the function in a small program that allows users to query the function from the command line.
* Users shall provide the word as a string and the location as xy-coordinates along direction 'A' for across or 'D' for down
* Assume that players do not understand 0-based indexing so valid coordinates will range from 1 to 15
* Blank squares (wildcards) should be indicated with an underscore character
* Invalid words must be given a score of -1
* Assume a standard 15x15 Scrabble board with certain squares having bonus multipliers
* Assume the standard Scrabble tiles with scores (e.g., A=1, B=3, C=3, ... X=8, y=4, Z=10)
* Enforce the standard Scrabble tile counts (e.g., there are four 'U' tiles and, two 'V' tiles, one 'X' tile, etc)
* Although a player's hand can only contain 7 tiles, letters can be added to existing tiles... so allow words up to 15 characters long (i.e., the board size)

## Examples ##
Here are four sample runs that show two valid words (one with a wildcard) and two invalid words.
* Valid word: $Zebra:1,2,A \rightarrow 2 \cdot (10 + 1 + 3 + 1 + 1) = 32$
* Valid word: $Ze\\_ra:7,8,D \rightarrow (10 + 2 \cdot 1 + 0 + 1 + 1) = 14$
* Invalid word: $Zabre:2,3,D \rightarrow -1$
* Out of bounds: $Zebra:14,3,A \rightarrow -1$

## Resources ##
The Scrabble Word Score Calculator will need a list of approved words that it can use to verify user input. The official Scrabble dictionary is available to members of the North American Scrabble Players Association (NASPA) as a text file; however, it is not released to the public. Therefore, this project will use a publically available dictionary obtained from DWYL's github repository. DWYL posted a text file containing 479k English words based on a file from Info Chimps. **Warning:** there are "words" in this file that are obviously not real words... but it's a reasonable dictionary in the public domain.
* [words_alpha.txt](words_alpha.txt)
