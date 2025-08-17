# Primenumber Generator #
Write a program that will generate a large prime numbers.

Prime numbers are an important part of public key cryptography, a key technology that protects e-commerce, email, and  other important communications. Prime numbers are integers that cannot be evenly divided by any number except for 1 and themselves: 2, 3, 5, 7, 11, 13, 17, 19, 23, and so on. Cryptography relies on very large prime numbers.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Write a brute force algorithm to determine if a number $n$ is prime.
   - Use the modulus operator to determine if one number is evenly divisible by another.
   - Ouptut a short message that states whether the number is prime or composite.
   - It is acceptable to handle a few special cases manually.
   - Hardcode a few tests with both primes and non-primes to make sure that the algorithm works correctly.

2. ***Script Kiddie***:  
   Save every calculated prime number to a text file.
   - Before running the slow brute force algorithm, check if the number $n$ is contained in the file.
   - The output must specify whether the answer came from the cache or was calculated with brute force.
   - Continue using hardcoded values to test $n$.

3. ***Professional***:  
   Improve the brute force algorithm to use the Sieve of Erathosthenes and add command line parameters.
   - Use a positional command line parameter to specify $n$.
   - If $n$ is contained in the text file, print the cached value.
   - Otherwise, generate a Sieve of Eratosthenes to calculate all the prime numbers between $2$ and $n$ and print out the largest prime that is less than or equal to $n$. Save this new prime number to the text file.

4. ***1337 H@cker***:  
   Modify the command line to take two arguments, $m$ (required) and $n$ (optional).
   - If $n$ is provided, print all of the prime numbers between $m$ and $n$, inclusive.
   - If $n$ is omitted, print the largest prime that is less than or equal to $m$, using the cache file as described previously.

5. ***BONUS***:  
   Replace the code for the Sieve of Eratosthenes with the faster Sieve of Atkin.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to lookup basic features and examples of the programming language. For example, a student might ask AI for the modulus operator in a certain language. For most languages, the AI should respond that the modules operator is the percent sign (`%`) and can be used as shown: `modulus = number % divisor`.

However, students are prohibited from giving the AI with any information about the project. If the AI guesses the context of the assignment and provides sample code, please try to ignore this information. Basically, studnets may use AI as a nice interface to the official documentation but may not use AI to write any of the project.

## Constraints ##
None.

## Examples ##
```
user@computer:~$ python prime.py
1 is not prime and not composite
2 is prime
3 is prime
4 is composite
7 is prime
13 is prime
25 is composite
100 is composite

user@computer:~$ python prime.py
1 is not prime and not composite
2 is prime (cache)
3 is prime (cache)
4 is composite
7 is prime (cache)
13 is prime (calculated)
25 is composite
100 is composite

user@computer:~$ python prime.py 13
13 is Prime (cache)

user@computer:~$ python prime.py 17
17 is Prime (calculated)

user@computer:~$ python prime.py 1 100
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
```

## Resources ##
* [https://www.baeldung.com/cs/prime-number-algorithms](Akbar Karimi's Fastest Algorithms to Find Prime Numbers)
* [https://en.wikipedia.org/wiki/Generation_of_primes](Wikipedia's "Generation of Primes" Page)