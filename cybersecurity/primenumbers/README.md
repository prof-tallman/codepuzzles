# Primenumber Generator #
Write a program that will generate a large prime numbers.

Prime numbers are an important part of public key cryptography, a key technology that encrypts e-commerce, email, and  other important communications. Prime numbers are integers that cannot be evenly divided by any number except for 1 and themselves: 2, 3, 5, 7, 11, 13, 17, 19, 23, and so on. Cryptography relies on very large prime numbers.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.
1. ***AI Does My HW***: Write a brute force algorithm to determine if a number $n$ is prime. Use the modulus operation to determine if one number is evenly divisible by another. Hardcode a few primes and non-primes to make sure that the algorithm works correctly.
2. ***Script Kiddie***: Use the Sieve of Eratosthenes to generate all the prime numbers between $2$ and $n$. If $n$ is *not* a prime number, print out the largest prime that is less than $n$. Continue using hardcoded values for $n$.
3. ***Professional***: Save every calculated prime number to a text file. Before running the slow Sieve of Eratosthenes, check if the number $n$ is contained in the file. If it's not in the file, run the Erathosthenes Algorithm. Instead of using hardcoded values for $n$, use a command line argument.
4. ***1337 H@cker***: Modify the command line to take two arguments, $m$ and $n$. Find all of the prime numbers between $m$ and $n$ and randomly print one of them. If there are no primes, print the largest prime that is less than $m$
5. ***BONUS***: Replace the code for the Sieve of Eratosthenes with the faster Sieve of Atkin.

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