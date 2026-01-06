# N-Gram Calculator #
Calculate the frequency of n-grams in a text file.

Many of the history's most famous code breakers used frequency analysis to crack the code. These super hackers would calculate how often certain letters, or sequences of letters called n-grams, would appear in ciphertext. They knew the standard n-gram distribution for the English language (or whatever language they were working in), and could work backward to decrypt the message without knowing the secret key.

The term n-gram is generic and it represents a sequence of letters of arbitrary length. Some specific n-grams are digrams and trigrams, which are two and three letter sequences, respectively.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Calculate the frequency of each letter in a string.
   - Write a function that will calculate the frequency of letter a-z within a text string.
   - Return the result as either a 26-element list or as a dictionary.
   - Call this function with a hardcoded text message that contains lower-case letters *only*.
   ```
   user@computer:~$ python ngrams.py
   Text: aaaaabbbbcccdefghijklmnopqrstuvwxyz
   {'a': 14.3, 'b': 11.4, 'c': 8.6, 'd': 2.9, 'e': 2.9, 'f': 2.9, 'g': 2.9, 'h': 2.9,
   'i': 2.9, 'j': 2.9, 'k': 2.9, 'l': 2.9, 'm': 2.9, 'n': 2.9, 'o': 2.9, 'p': 2.9,
   'q': 2.9, 'r': 2.9, 's': 2.9, 't': 2.9, 'u': 2.9, 'v': 2.9, 'w': 2.9, 'x': 2.9,
   'y': 2.9, 'z': 2.9}

   user@computer:~$ python ngrams.py
   Text: aaaaabbbbcccdefghijklmnopqrstuvwxyz
   [14.3, 11.4, 8.6, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9,
   2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9}
   ```

2. ***Script Kiddie***:  
   Add digram and trigram frequency counters.
   - Write a second function that will calculate the frequency of each digram.
   - Write a third function that will return the frequency of every trigram.
   - For each function, return the results in a dictionary.
   - Pass the same hardcoded text message to each of these functions and make sure that they return the correct results.
   ```
   user@computer:~$ python ngrams.py
   Text: aaaaabbbbcccdefghijklmnopqrstuvwxyz
   {'a': 14.3, 'b': 11.4, 'c': 8.6, 'd': 2.9, 'e': 2.9, 'f': 2.9, 'g': 2.9, 'h': 2.9,
   'i': 2.9, 'j': 2.9, 'k': 2.9, 'l': 2.9, 'm': 2.9, 'n': 2.9, 'o': 2.9, 'p': 2.9,
   'q': 2.9, 'r': 2.9, 's': 2.9, 't': 2.9, 'u': 2.9, 'v': 2.9, 'w': 2.9, 'x': 2.9,
   'y': 2.9, 'z': 2.9}
   {'aa': 11.8, 'ab': 2.9, 'bb': 8.8, 'bc': 2.9, 'cc': 5.9, 'cd': 2.9, 'de': 2.9,
   'ef': 2.9, 'fg': 2.9, 'gh': 2.9, 'hi': 2.9, 'ij': 2.9, 'jk': 2.9, 'kl': 2.9,
   'lm': 2.9, 'mn': 2.9, 'no': 2.9, 'op': 2.9, 'pq': 2.9, 'qr': 2.9, 'rs': 2.9,
   'st': 2.9, 'tu': 2.9, 'uv': 2.9, 'vw': 2.9, 'wx': 2.9, 'xy': 2.9, 'yz': 2.9}
   {'aaa': 9.1, 'aab': 3.0, 'abb': 3.0, 'bbb': 6.1, 'bbc': 3.0, 'bcc': 3.0, 'ccc': 3.0,
   'ccd': 3.0, 'cde': 3.0, 'def': 3.0, 'efg': 3.0, 'fgh': 3.0, 'ghi': 3.0, 'hij': 3.0,
   'ijk': 3.0, 'jkl': 3.0, 'klm': 3.0, 'lmn': 3.0, 'mno': 3.0, 'nop': 3.0, 'opq': 3.0,
   'pqr': 3.0, 'qrs': 3.0, 'rst': 3.0, 'stu': 3.0, 'tuv': 3.0, 'uvw': 3.0, 'vwx': 3.0,
   'wxy': 3.0, 'xyz': 3.0} 
   ```

3. ***Professional***:  
   Calculate the frequency of n-grams from a text file that was given as a command line parameter.
   - Instead of passing a hardcoded message to each function, read the message from a text file.
   - Start by hardcoding the name of the text file. Then change the program to take a command line argument that contains the name of the text file.
   - Print all of the results.
   Handle text that includes mixed-case letters, numbers, and punctuation. Remove all of the non-alphabetic characters so that the three functions treat the text as one giant string of letters.
   ```
   user@computer:~$ python ngrams.py
   usage: ngrams3.py [-h] file
   ngrams3.py: error: the following arguments are required: file

   user@cmoputer:~$ python ngrams.py dne.txt
   Error: the file 'dne.txt' does not exist

   user@computer:~$ cat test.txt
   This is the content in my test file.

   user@computer:~$ python ngrams.py test.txt
   Text: thisiscontentinmytestfile
   {'a': 0.0, 'b': 0.0, 'c': 4.0, 'd': 0.0, 'e': 12.0, 'f': 4.0, 'g': 0.0, 'h': 4.0,
   'i': 16.0, 'j': 0.0, 'k': 0.0, 'l': 4.0, 'm': 4.0, 'n': 12.0, 'o': 4.0, 'p': 0.0,
   'q': 0.0, 'r': 0.0, 's': 12.0, 't': 20.0, 'u': 0.0, 'v': 0.0, 'w': 0.0, 'x': 0.0,
   'y': 4.0, 'z': 0.0}
   {'th': 4.17, 'hi': 4.17, 'is': 8.33, 'si': 4.17, 'sc': 4.17, 'co': 4.17, 'on': 4.17,
   'nt': 8.33, 'te': 8.33, 'en': 4.17, 'ti': 4.17, 'in': 4.17, 'nm': 4.17, 'my': 4.17,
   'yt': 4.17, 'es': 4.17, 'st': 4.17, 'tf': 4.17, 'fi': 4.17, 'il': 4.17, 'le': 4.17}
   {'thi': 4.35, 'his': 4.35, 'isi': 4.35, 'sis': 4.35, 'isc': 4.35, 'sco': 4.35,
   'con': 4.35, 'ont': 4.35, 'nte': 4.35, 'ten': 4.35, 'ent': 4.35, 'nti': 4.35,
   'tin': 4.35, 'inm': 4.35, 'nmy': 4.35, 'myt': 4.35, 'yte': 4.35, 'tes': 4.35,
   'est': 4.35, 'stf': 4.35, 'tfi': 4.35, 'fil': 4.35, 'ile': 4.35}
   ```

4. ***1337 H@cker***:  
   Combine the three redundant functions into one master function.
   - Right now the program uses three separate functions to calculate single letter frequencies, digrams, and trigrams.
   - Analyze these three functions and figure out how to write a single function that will calculate the frequency of any length n-gram.
   - Pass the desired n-gram length as a parameter to this function.
   
6. ***BONUS***:  
   Print the output to the console window starting with the most common n-gram and continuing with the full top-10 results in decreasing order. Do not print anything beyond the top-10 reuslts.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to lookup basic features and examples within the programming language. For example, somebody might ask AI how to read a text file. The AI would most likely respond by explaining how to use functions like `read` (for Python) or `ReadTextFile` for C#.

However, students are prohibited from giving the AI with any information about the project. If the AI guesses the context of the assignment and provides sample code, please try to ignore this information. Basically, studnets may use AI as a nice interface to the official documentation but may not use AI to write any of the project.

## Constraints ##
Additional assumptions and constraints are listed below.
* If the user specifies a file that does not exist, handle the error gracefully by printing a helpful message and then quitting.
* Ignore capatilization: `a` is the same as `A`.
* For single-letter frequencies, include all 26 letters of the alphabet, even if a particular letter is missing. The frequency of a missing letter is `0.0`.
* For digrams, trigrams, and beyond, only include the n-grams that are included in the message. The n-grams that are missing from the input text should be omitted from the output.
* Calculate each frequency as a percentage and round to 2 decimal points (e.g., $0.1234 \rightarrow 0.12$)

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
