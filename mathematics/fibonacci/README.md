# Fibonacci Generator #
The Fibonacci Sequence is an infinite series of numbers starting at 1. Well, it actually begins with *two* values, both 1 and 1. The next number in the sequence is the sum of the two previous. For example, the third number in the sequence is $2$ since $1+1=2$; then it goes on to $1+2=3$, $2+3=5$, and so on. The first ten values in the Fibonacci Sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. The sequence starts small but gets big quickly. The Fibonacci Sequence is particularly interesting because it is commonly found in nature and has artistic applications.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Write a program that calculates and prints the first 10 Fibonacci numbers.
   - Use a function that returns the sequence as a list.
   - Call the function and then print out the entire list.
   ```
   user@computer:~$ python fib.py
   1
   1
   2
   3
   5
   8
   13
   21
   34
   55
   ```

2. ***Script Kiddie***:  
   Let the user decide how long the sequence should be.
   - Modify the function to accept a parameter $n$ that indicates the length of the Fibonacci sequence.
   - The function must return a list of length $n$.
   - The user should specify $n$ at the command line.
   ```
   user@computer:~$ python fib.py 5
   1
   1
   2
   3
   5
   ```

3. ***Professional***:  
   Add a verbose mode and make the Fibonacci generator more memory-efficient when possible.
   - Accept a flag `-v` or `--verbose` command line flag to control output.
   - Without `--verbose`, print only the nth Fibonacci number.
   - With `--verbose`, print the entire sequence up to $n$.
   - Use two different functions:
     - One that returns the whole list (for verbose mode).
     - One that calculates the th Fibonacci number using a loop with no more than 3 temporary variables (plus the loop counter). No list storage is allowed.
   - Print large results with a comma between every three digits.
   ```
   user@computer:~$ python fib.py 10
   55
   
   user@computer:~$ python fib.py 100
   354,224,848,179,261,915,075
   
   user@computer:~$ python fib.py 5 --verbose
   1
   1
   2
   3
   5
   ```

4. ***1337 H@cker***:  
   Add a recursive option and make the program bulletproof against bad input.
   - Accept the `-r` / `--recursive` flag to calculate the sequence using a **recursive** formula.
   - Prevent the `--recursive` and `--verbose` flags from being used simultaneously.
   - The program should now have three different Fibonacci functions (list-returning, memory-efficient iterative, and recursive).
   - All three functions should produce the same value for the requested Fibonacci element $n$
   - Perform error checking on the argument $n$ to make sure that it is valid. If the $n$ is unacceptable, quit gracefully with an error message explaining why the value of $n$ does not work so that other computer science students will understand.
   ```
   user@computer:~$ python fib.py 100
   354,224,848,179,261,915,075
   
   user@computer:~$ python fib.py 5 --verbose
   1
   1
   2
   3
   5

   user@computer:~$ python fib.py 30 --recursive
   Wait for it...
   832,040

   user@computer:~$ python fib.py 0
   Element 0 is invalid, the sequence begins at element 1
   ```

5. ***BONUS***:
   Use a simple drawing library to generate a picture that illustrates the Fibonacci Sequence up to degree $n$. For example, draw a spiral where each square's side length matches a Fibonacci number.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to lookup basic features and examples within the programming language. For example, somebody might ask AI how to convert from a string to a number. Most AIs would point the person towards the `int()` function in python or the `Int.Parse()` function in C#.

However, students are prohibited from providing the AI with any information about the project. If the AI guesses the context of the assignment and provides sample code, please try to ignore this information. Basically, students may use AI as a nice interface to the official documentation but may not use AI to write any of the project.

## Constraints ##
None at this time.

## Resources ##
Students who are attempting the bonus should consider using GUI libraries such as Python's TkInter module or the C#'s .NET MAUI.
