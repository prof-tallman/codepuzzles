# Password Complexity Checker #
Determine if a password fulfills a set of complexity requirements.

Passwords are used to authenticate a person based on some secret information that they have memorized. An adversary who knows a victim's password can impersonate the victim and gain access to the protected resource. So it is important to choose strong passwords that cannot be easily guessed. To help enforce strong passwords, many programs require a certain level of password complexity. Passwords that do not meet the complexity requirements are not allowed.

Note: This project is a fun challenge but the program will not adequately protect the user's input. Do not type in the real password for any bank account, school account, or other important resource.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Create a simple password complexity checker.
   - Write a function that will return True/False whether a potential password is at least 8 characters long and contains at least one uppercase letter, one lowercase letter, and one number.
   - Call this function with a few hardcoded sample passwords. Some passwords should meet the complexity requirements and others should purposely fail. Remember, it is a good thing for simple passwords to fail the complexity check.
   ```
   user@computer:~$ python pwdfilter.py
   aaaBBB111           : PASS (as expected)
   pAssw0rd            : PASS (as expected)
   1reallyLONGpassword : PASS (as expected)
   1tW0rks!            : PASS (as expected)
   Short1              : FAIL (as expected)
   lowercase           : FAIL (as expected)
   UPPERCASE           : FAIL (as expected)
   NoNumber            : FAIL (as expected)
   ```

2. ***Script Kiddie***:  
   Hide the password on the screen so that eavesdroppers cannot read it.
   - Replace the hardcoded passwords with a user prompt. When the user types their password, it will show on the screen (oops)!
   - Instead of using the regular input function, use a module like `getpass` to hide or mask the letters typed by the user (you'll have to research `getpass` or some other equivalent)
   - In addition to the three previous character classes, also require the password to include a symbol like !@#$%^&*().
   - Note: in the example below, the user's input was hidden by the `getpass` module.
   ```
   user@computer:~$ python pwdfilter.py
   Password: (the user typed '123qweASD' but the text was hidden)
   Oops, that password does not pass the complexity requirements
   
   user@computer:~$ python pwdfilter.py
   Password: (the user typed '123qweASD@' but the text was hidden)
   Congratulations, your password is sufficiently complex
   ```

3. ***Professional***:  
   Track password history and prevent users from reusing a previous password.
   - Keep track of the last five passwords in a text file.
   - If the current password is contained in the text file, reject it as an unsafe password.
   - Seed the history file with five passwords.
   - Every time that a new password meets the complexity requirements, it is added to the history file and the oldest password on the list is removed.
   - If the password is ever rejected, explain to the user what is wrong with it. Use custom exception messages, but exit gracefully. If there are multiple problems with a password, pointing out one of the problems is sufficient.
   ```
   user@computer:~$ python pwdfilter.py
   Password: (the user typed '123qweASD' but the text was hidden)
   Error: Password must contain a symbol '!@#$%^&*()'

   user@computer:~$ python pwdfilter.py
   Password: (the user typed '123qwe!@#' but the text was hidden)
   Error: Password must contain an uppercase letter

   user@computer:~$ python pwdfilter.py
   Password: (the user typed '123' but the text was hidden)
   Error: Password must be at least 8 characters

   user@computer:~$ python pwdfilter.py
   Password: (the user typed '123qweASD@' but the text was hidden)
   Password meets complexity requirements
   
   user@computer:~$ cat pwdhistory.txt
   pAssw0rd
   1reAllyLoNGpaSsw0rd
   1tW0rks!
   tr0ubl3$
   123qweASD@

   user@computer:~$ python pwdfilter.py
   Password: (the user typed '123qweASD@' but the text was hidden)
   Error: Password was found in history file
   ```

4. ***1337 H@cker***:  
   Improve account security by requiring stricter passwords. Critical resources are usually protected with highly complex passphrases.
   - Restrict the passwords further so that they cannot contain more than three consecutive characters from the same class (in other words, no more than three lowercase letters in a row or no more than three numbers in a row).
   ```
   user@computer:~$ python pwdfilter.py
   Password: (the user typed 'Password123!' but the text was hidden)   
   Error: Password contains more than 3 lowercase characters in a row

   user@computer:~$ python pwdfilter.py
   Password: (the user typed 'Pas1!Pas1!!' but the text was hidden)   
   Password meets complexity requirements
   ```

5. ***BONUS***:  
   Prevent adversaries from stealing passwords that are in the history file by encrypting each password. The passwords may be encrypted with a cryptographic hash or a simple encryption algorithm. Import an existing algorithm, do not copy or create one from scratch.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to look up basic features and examples within the programming language. For example, somebody might ask AI how to find the length of a string. If the program was being written in C, the AI would likely mention the `strlen()` function. On the other hand, if the programming language was Python, then the AI would almost certainly explain how to use the built-in `len()` function.

However, students are prohibited from providing the AI with any information about the project. If the AI guesses the context of the assignment and provides sample code, please try to ignore this information. Basically, students may use AI as a nice interface to the official documentation but may not use AI to write any of the project.

## Constraints ##
Additional assumptions and constraints are listed below.
* Restrict all passwords to English characters, including numbers and punctuation. Passwords can be written in any language and some password algorithms even allow for non-printable characters. But this puzzle should be solved for English characters only.

## Resources ##
Additional resources are not necessary to complete this project.
