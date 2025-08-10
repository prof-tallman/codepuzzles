# Primenumber Generator #
Write a program that will generate a large prime numbers.

Prime numbers are an important part of public key cryptography, a key technology that encrypts e-commerce, email, and  other important communications. Prime numbers are integers that cannot be evenly divided by any number except for 1 and themselves: 2, 3, 5, 7, 11, 13, 17, 19, 23, and so on. Cryptography relies on very large prime numbers.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.
1. ***AI Does My HW***: Write a brute force algorithm to determine if a number $n$ is prime. Use the modulus operation to determine if one number is evenly divisible by another. It is likely that you will need handle a few special cases manually. Hardcode a few tests with both primes and non-primes to make sure that the algorithm works correctly.
2. ***Script Kiddie***: Save every calculated prime number to a text file. Before running the slow brute force algorithm, check if the number $n$ is contained in the file. Continue using hardcoded values to test $n$.
3. ***Professional***: Use a command line parameter instead of a hardcoded value for $n$. If $n$ is contained in the text file, print the cached value. Otherwise, generate the Sieve of Eratosthenes to generate all the prime numbers between $2$ and $n$ and print out the largest prime that is less than equal to $n$. Save this new value to the text file if it is not there already.
4. ***1337 H@cker***: Modify the command line to take two arguments, $m$ (required) and $n$ (optional). If $n$ is provided, print all of the prime numbers between $m$ and $n$. If $n$ is omitted, print the largest prime that is less than or equal to $m$, using the cache file as described previously.
5. ***BONUS***: Replace the code for the Sieve of Eratosthenes with the faster Sieve of Atkin.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to lookup basic features and examples of the programming language. For example, a student might ask AI for the modulus operator in a certain language. For most languages, the AI should respond that the modules operator is the percent sign (`%`) and can be used as shown: `modulus = number % divisor`.

However, students are prohibited from giving the AI with any information about the project. If the AI guesses the context of the assignment and provides sample code, please try to ignore this information. Basically, studnets may use AI as a nice interface to the official documentation but may not use AI to write any of the project.

## Constraints ##
None.

## Examples ##
```
user@computer:~$ python prime.py 1 100
47
user@computer:~$ python prime.py 1 100
3
user@computer:~$ python prime.py 1 100
71
user@computer:~$ python prime.py 48 50
47
```

## Resources ##
* [https://www.baeldung.com/cs/prime-number-algorithms](Akbar Karimi's Fastest Algorithms to Find Prime Numbers)
* [https://en.wikipedia.org/wiki/Generation_of_primes](Wikipedia's "Generation of Primes" Page)