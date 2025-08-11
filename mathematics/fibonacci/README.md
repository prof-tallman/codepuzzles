# Fibonacci Generator #
The Fibonacci Sequence is a series of numbers starting at 1 and 1. The next number in the sequence is the sum of the two previous numbers. For example, $1+1=2$, which goes on to $1+2=3$, then $2+3=5$ and so on. The first ten numbers in the Fibonacci Sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. The sequence starts small but gets big quickly. The Fibonacci Sequence is particularly interesting because it is commonly found in nature and has artistic applications.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
  Write a program that calculates and prints the first 10 Fibonacci numbers.
  
  **Requirements:**
  - Use a function that returns the sequence as a list.
  - Call the function and then print out the entire list.

2. ***Script Kiddie***:  
Let the user decide how long the sequence should be.
**Requirements:**
*Modify the function to accept a parameter $n$ that indicates the length of the Fibonacci sequence.
*Your function must return a list of length $n$.
*The user should specify $n$ at the command line.

3. ***Professional***:  
Add a verbose mode and make your Fibonacci generator more memory-efficient when possible.
**Requirements:**
*Accept a `-v` or `--verbose` command line flag to control output.
*Without `--verbose`, print only the nth Fibonacci number.
*With `--verbose`, print the entire sequence up to $n$.
*Use two different functions:
**One that returns the whole list (for verbose mode).
**One that calculates the nth Fibonacci number using a loop with no more than 3 temporary variables (plus the loop counter) — no list storage allowed.

4. ***1337 H@cker***:  
Add a recursive option and make your program bulletproof against bad input.
**Requirements:**
*Accept a `-r` or `--recursive` flag to calculate the sequence using a **recursive** formula.
*Your program should now have three different Fibonacci functions (list-returning, memory-efficient iterative, and recursive).
*Perform error checking on the argument $n$ to make sure that it is valid. If the $n$ is unacceptable, quit gracefully with an error message explaining why the value of $n$ does not work so that other computer science students will understand.

5. ***BONUS***:
Use a simple drawing library to generate a picture that illustrates the Fibonacci Sequence up to degree $n$. For example, draw a sprial where each square's side length matches a Fibonacci number.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to lookup basic features and examples within the programming language. For example, somebody might ask AI how to convert from a string to a number. Most AIs would point the person towards the `int` function in python or the `Int.Parse` function in C#.

However, students are prohibited from giving the AI with any information about the project. If the AI guesses the context of the assignment and provides sample code, please try to ignore this information. Basically, students may use AI as a nice interface to the official documentation but may not use AI to write any of the project.

## Constraints ##
None at this time.

## Examples ##
Here are a few sample runs for the final program.
```
user@computer:~$ python fibonacci.py 8
21

user@computer:~$ python fibonacci.py 8 --verbose
1, 1, 2, 3, 5, 8, 13, 21

user@computer:~$ python fibonacci.py 8 --recursive
21 (using recursive codepath)

user@computer:~$ python fibonacci.py -3
Error: The Fibonacci Sequence is not defined for negative numbers.

```

## Resources ##
If you are attempting the bonus, you might consider using Python with the TkInter module.