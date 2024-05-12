# Password Complexity Checker #
Determine if a passphrase fulfills a set of complexity requirements.

Passwords are used to authenticate a person based on some secret information that they have memorized. But any adversary that can guess somebody's password can gain access to the protected resource. So it is important to choose a password that cannot be easily guessed. To help with this, many programs require a certain level of password complexity. Passwords that do not meet the complexity requireements are not allowed.

Note: This program is a fun challenge but does not adequetly protect the user's input. Do not type in a password for your bank account or some other important resource.

## Stages ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.
1. Write a function that will return whether a potential password is at least 8 characters long and contains at least one uppercase letter, one lowercase letter, one number, and one symbol. Call this function with a few hardcoded sample passwords that meet the requirements and others that fail.
2. Replace the hardcoded passwords with a user input prompt that masks the letters typed by the user. This should help protect the user against any adversaries that might look over their shoulder.
3. Keep track of the last 10 passwords in a text file. If the current password is contained in the text file, reject it as an unsafe password. Seed the history file with 10 passwords. Every time that a new password is entered, it is added to the top of the list and the last password on the list is removed.
4. Critical resources are usually protected with highly complex passphrases. Restrict the passwords so that they cannot contain more than three consecutive characters from the same class. In other words, no more than three lowercase letters in a row or no more than three numbers in a row.
BONUS: Prevent adversaries from stealing passwords that are in the history file by encrypting each password. The passwords may be encrypted with a cryptographic hash or a simple encryption algorithm. Import an existing algorithm, do not copy or create one from scratch.

## Constraints ##
Additional assumptions and constraints are listed below.
* Restrict all passwords to English characters, including numbers and punctuations. Passwords can be written in any language and some password algorithms even allow for non-printable characters. But this puzzle should be solved for English characters only.

## Examples ##
Here are five sample runs that show two valid passwords and two invalid passwords.
* Valid password: `d@ng3rouS`<br>
Explanation: pasword is longer than 8 characters and includes 1 symbol, 1 number, 1 uppercase letter, and 6 lowercase letters but no more than 3 in a row.
* Valid password: `2leg!t2QU!T`<br>
Explanation: pasword is longer than 8 characters and includes 1 symbol, 1 number, 1 uppercase letter, and 6 lowercase letters but no more than 3 in a row.
* Invalid password: `1q@W`<br>
Explanation: password is fewer than 8 characters.
* Invalid password: `Marty3@gle`<br>
Explanation: password contains more than 3 lowercase letters in a row.
* Invalid password: `Pwd12345`<br>
Explanation: password does not contain a symbol

## Resources ##
Additional resources are not necessary to complete this project.
