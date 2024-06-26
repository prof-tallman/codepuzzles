# N-Gram Calculator #
Calculate the frequency of n-grams in a text file.

Many of the most history's most famous code breakers used frequency analysis to crack ciphers. These super hackers would calculate how often certain letters, or sequences of letters called n-grams, would appear in ciphertext. They knew the standard n-gram distribution for the English language (or whatever language they were working in), and could work backward to decrypt the message without knowing the secret key.

The term n-gram is generic and it represents a sequence of letters of arbitrary length. Some specific n-grams are digrams and trigrams, which are two and three letter sequences, respectively.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.
1. ***AI Does My HW***: Write a function that will calculate the frequency of each single letter a-z within a text string. Return the result as either a 26-element list or a dictionary. Call this function with a hardcoded text message.
2. ***Script Kiddie***: Write a second function that will calculate the frequency of each digram; write a third function that will return the frequency of every trigram. Return the result in a dictionary. Pass the same hardcoded text to each of these functions.
3. ***Professional***: Instead of passing a hardcoded message to each of your functions, read the message from a text file. Start by hardcoding the name of the text file. Then change the program to take a command line argument that contains the name of the text file.
4. ***1337 H@cker***: Right now the program uses three separate functions to calculate single letter frequencies, digrams, and trigrams. Analyze these three functions and figure out how to write a single function that will calculate the frequency of any length n-gram.
5. ***BONUS***: Print the output to the console window starting with the most common n-gram and continuing with the top-15 results in decreasing order. Do not print anything beyond the top-15 reuslts.

## Constraints ##
Additional assumptions and constraints are listed below.
* If the user specifies a file that does not exist, handle the error gracefully by printing a helpful message and then quitting.
* Ignore capatilization: `a` is the same as `A`.
* For single-letter frequencies, include all 26 letters of the alphabet, even if a particular letter is missing. The frequency of a missing letter is `0.0`.
* For digrams, trigrams, and beyond, only include the n-grams that are included in the message. The n-grams that are missing from the input text should be omitted from the output.
* Calculate each frequency as a percentage and round to 1 decimal point (e.g., $0.1234 \rightarrow 12.3$)

## Examples ##
If the input text was "The quick red fox jumped over the lazy dog", then some of the n-gram frequency distributions would be:
| Letter Frequencies | Digrams | Trigrams |
|--------------------|---------|----------|
|`A:2.8`|`th:5.7`|`the:5.9`|
|`B:0.0`|`he:5.7`|`heq:2.9`|
|`C:2.8`|`eq:2.9`|`equ:2.9`|
|`D:8.3`|`qu:2.9`|`qui:2.9`|
|`E:11.1`|`ui:2.9`|`uic:2.9`|
|`...`|`...`|`...`|

## Resources ##
Additional resources are not necessary to complete this project.