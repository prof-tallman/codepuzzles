# Jaccard Index #
Compute how similar two texts are using the Jaccard index.

The Jaccard coefficient measures the overlap between two sets. It is:

𝐽
(
𝐴
,
𝐵
)
=
∣
𝐴
∩
𝐵
∣
∣
𝐴
∪
𝐵
∣
J(A,B)= 
∣A∪B∣
∣A∩B∣
​
 
For example, if set #1 is {A, B, F, H, T, Y} and set #2 is {B, C, F, G, S, Y}, then the intersection is {B, F, Y} (3 elements) and the union is {A, B, C, F, G, H, T, Y} (8 elements). So 
𝐽
=
3
/
8
=
0.375
J=3/8=0.375.

In this project, you’ll take two inputs (strings or files), turn them into sets (characters, words, or n-grams), and calculate their Jaccard similarity. You’ll also add flags to control how the sets are built and how results are displayed.



## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Compute Jaccard similarity for two short strings using distinct characters only.
   - Write a function `jaccard_chars(a, b)` that:
     - Converts each input string `a` and `b` to a set of characters.
     - Returns the Jaccard coefficient as a float $\frac{|A \cap B|}{|A \cup B|}$
     - In main, call the function with two hardcoded test strings (letters only; no spaces/punctuation) and print the similarity rounded to 3 decimals.
     - If either set is empty, define $J=0.0$.

2. ***Script Kiddie***:
   Let the user supply the inputs and choose how sets are built.
   - Read two inputs from the command line (quoted if they contain spaces), e.g. `python jaccard.py "abc" "bcd"`.
   - Add a `--words` flag that changes between:
     - (omitted): set of distinct characters.
     - `--words`: set of distinct words split on whitespace.
   - Print the Jaccard coefficient rounded to 3 decimals.

3. ***Professional***:
   Add n-grams, explanations, and distance. Make the tool robust and helpful.
   - Add a new command line option `--ngrams N` (integer ≥ 2) to build character n-grams when `--mode chars`, or word n-grams when `--mode words`.
     - Example (chars, N=3): `'hello world!'` → [ `hel`, 'lo ', 'wor', 'ld!' ]
     - Example (words, N=2): `'to be or not to be'` → `to be`, `or not`, `to be`
   - Add `--explain` to print: |A|, |B|, |A∩B|, |A∪B| A sorted list (or capped count) of the intersection and union elements.
   - Add `--distance` to also print Jaccard distance, which is defined as $1−J$.

4. ***1337 H@cker***:
   Scale up: compare multiple documents and report the most similar pair(s).
   - Accept `--files file1 file2 ... fileK` to read K ≥ 2 text files instead of two strings. If the `--files` flag parameter is used, the program will ignore the two strings.
   - Build sets for each file using the same flags as above (--mode, --ngrams, --case-insensitive, --clean).
   - Compute the pairwise Jaccard similarity for all possible file pairs.
   - Handle file errors gracefully (e.g., if a file is missing, or unreadable, or empty).

5. ***BONUS***:
   Add a brute-force directory mode using a new command line flag `--dir PATH` that reads all of the `*.txt` files in a directory and runs the top-3 report on them.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to look up basic features and examples within the programming language. For example, someone might ask how to split a string into words, how to read a file, or how to round a float.

However, students are prohibited from giving the AI any information about the project. If the AI guesses the context and provides sample code, please ignore it. Basically, students may use AI as a convenient interface to official documentation but may not use AI to write any of the project.

## Constraints ##
Additional assumptions and constraints are listed below.
- Treat inputs as sets (no duplicates) unless --weighted is used.
When --words, split on whitespace by default; you may also normalize multiple spaces.
If --clean alpha is set, strip all characters except [A-Za-z] before tokenization.
For empty sets on both sides, define $J=0.0$.
- Round all printed numbers to 3 decimals.
- Use clear, actionable error messages and exit codes for invalid arguments.

## Examples ##
Here are a few sample runs for the final program.
```
user@computer:~$ python jaccard.py "red the fox" "the fox is red" --words
0.750

user@computer:~$ python jaccard.py --files doc1.txt doc2.txt doc3.txt --words
Pairwise Jaccard (words):
doc1.txt vs doc2.txt: 0.612
doc1.txt vs doc3.txt: 0.427
doc2.txt vs doc3.txt: 0.398

user@computer:~$ python jaccard.py "ABFHTY" "BCFGSY"
0.333

user@computer:~$ python jaccard.py "ABFHTY" "BCFGSY"
|A| = 6
|B| = 6
|A ∩ B| = 3
|A ∪ B| = 9
Intersection A ∩ B: [ 'B', 'F', 'Y' ]
Union A ∪ B:        [ 'A', 'B', 'C', 'F', 'G', 'H', 'S', 'T', 'Y' ]
```

## Resources ##
You may find the [Jaccard Index Wikipedia Page|https://en.wikipedia.org/wiki/Jaccard_index] helpful.