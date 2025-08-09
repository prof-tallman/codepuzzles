# Caesar Shift Cipher #
Write a program that encrypts and decrypts text messages using the Caesar Shift Cipher.

The Caesar Shift Cipher is a historic cipher credited to the Roman military. It is considered one of the weaker ciphers to break since there are only 25 possible shift values (e.g., keys). However, the cipher has been used to encrypt military communications all the way up to the American Civil War.

The cipher works by rotating the entire alphabet forward so that each letter is shifted by the same amount. Plaintext letters at the end of the alphabet are wrapped around to ciphertext letters at the beginning of the alphabet. For example, if the shift amount is 5, then letter $A \rightarrow F$, $B \rightarrow G$, $C \rightarrow H$, $X \rightarrow C$, $Y \rightarrow D$, and $Z \rightarrow E$.

Decryption is the similar to encryption except that the alphabet is shifted in the opposite direction.

## Stages ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.
1. ***AI Does My HW***: Write a function that encrypts a text string by shifting each letter by a fixed amount. Return the encrypted string. Call this function with a hardcoded sample text and key. Compare the function's output to a precomputed test case that is known to be correct. For example, `hello` shifted by 5 would produce `mjqqt`. Do not inclue any spaces, punctuation, or numbers in the sample text--letters only.
2. ***Script Kiddie***: Add a decryption function that performs the inverse cipher operation. This can be accomplished quickly with just a few lines of code. Test the decryption function with the output of the encryption, it should return the original harcoded sample text. Do not include any spaces, punctuation, or numbers in the sample text--letters only.
3. ***Professional***: Change the program to use command line parameters instead of the hardcoded sample text. The program will need three parameters: the text to encrypt/decrypt, a key (the shift amount), and a flag to choose between encryption and decryption. Detect common errors and handle them gracefully. For example, what happens if the user passes in text that contains spaces or numbers?
4. ***1337 H@cker***: Modify the encryption and decryption functions to process spaces, punctuation, and numbers. The program should work in two modes: `simple` mode will include all non-alphabetic characters without changing them and `secure` mode will convert the text to uppercase and remove all spaces, punctuations, and numbers. Add another flag to the command line parameters that will choose between the two modes. 
5. ***BONUS***: Add a brute force option that will demonstrate the weakness of the Caesar Shift Cipher by printing the message using every possible shift value, 1-25.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to lookup basic features and examples within the programming language. For example, somebody might ask AI how to convert a letter to a number (in Python it would be the built-in `ord` function, or you could use a lookup string like `alphabet = 'abcdefghijklmnopqrstuvwxyz'` and the `find` function). Or, another student might ask how to convert a string entirely to uppercase (e.g., `text = text.upper()` in Python or `text = text.ToUpper()` in C#). Prompts like these are reasonable and allowed.

However, students are prohibited from giving the AI with any information about the project. If the AI guesses the context of the assignment and provides sample code, please try to ignore this information. Basically, studnets may use AI as a nice interface to the official documentation but may not use AI to write any of the project.

## Constraints ##
Additional assumptions and constraints are listed below.
* Although this cipher can be used for any alphabet-based language, it is reasonable to restrict your code to a single language such as English.
* Assume that the user will enter mixed-case text. That is, it might include lower-case and upper-case letters.

## Examples ##
Here are a few sample runs for the final program.
* Running in simple mode:
```
user@computer:~$ python caesar.py encrypt 'Hello world!' 5 simple
Mjqqt btwqi!
```
* Running in secure mode (notice that all letters are converted to upper case):
```
user@computer:~$ python caesar.py encrypt 'Hello world!' 5 secure
MJQQTBTWQI
```

## Resources ##
Additional resources are not required for this project.
