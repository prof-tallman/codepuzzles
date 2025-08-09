# Periodic Table Lookup #
Write a program that will calculate the molecular mass of a molecule.

The molecule should be written using standard chemical notation with uppercase and lowercase letters that specifies each individual element and the number of atoms that it contains. For example, water would be given as "H2O" and salt would be input as "NaCl".

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.
1. ***AI Does My HW***: Write a function that will parse a molecule string and print the individual elements and their quantities. Call this function with a few hardcoded modules to demonstrate that it works. The molecule can be restricted to single-letter elements like "H2O"; students are allowed to ignore molecules such as "NaCl" that contain atoms identified by multiple letters. The periodic table used by the program for lookups may either be provided as a hardcoded table or as a data file.
2. ***Script Kiddie***: Complete everything from the ***AI Does My HW*** program and then add a new feature that allows users to choose their own moecules. The program must accept molecules input at the command line parameters, it cannot rely on input functions in the code such as `input` (Python), ______ (Java), `ReadLine` (C#), or `gets` (C).
3. ***Professional***: Complete all of the requirements for the ***Script Kiddie*** version of this program. Improve the molecule parsing function so that it understands and properly calculates the mass of any/all elements in the periodic table. Make sure that the periodic table is read from a text file at runtime so that the program will be able to handle new, as of yet undiscovered elements simply by updating the periodic table text file.
4. ***1337 H@cker***:  In addition to completing all of the requirements for the ***Professional*** ranking, add a caching feature that will save the molecular formula and mass of any/all inputs to a text file. Every time that a new molecule is calculated--e.g., a molecule that is not already included in the cache--it will be calculated manually using your code and then the result will be saved to the cache. Before taking the time to run the slow manual calculation, the program should check the cache and, if the molecule exists in the cache, use the cached answer instead of parsing the input and running the calculation from scratch. If the program finds a molecule in the cache, it should include a short message explaining this in the output.
5. ***BONUS***: Modify the program to understand and properly parse nested submolecules such as ____________. The submolecule must be enclosed in parenthesis and the number immediately following the parenthesis specifies the number of submolecules included in the larger molecule.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to lookup basic features and examples within the programming language. For example, somebody might need to lookup the proper form of a for-loop that counts from 0 to n-1. Most AIs would answer with code like this (for the C programming language):
```
for(int i = 0; i < n; i++)
{
    // body of loop goes here
}
```

However, students are prohibited from giving the AI with any information about the project. If the AI guesses the context of the assignment and provides sample code, please try to ignore this information. Basically, studnets may use AI as a nice interface to the official documentation but may not use AI to write any of the project.

## Constraints ##
If a molecule specifies any elements that are not part the periodic table, the program should detect this error, print an error message, and exit gracefully.

Students with a chemistry background will be aware that there are physical properties that restrict the forming of molecules from arbitrary combinations of atoms. For example, ____________. Valitating the chemical validity of a given molecule is **not** required. Students are encouraged to simply read the individual elements and sum their masses, regardless of whether the elements form an actual molecule.

## Examples ##
```
joshua@laptop ~ % mcalc H2O
#####

joshua@laptop ~ % mcalc ASDFG
Error: molecule 'A' is not a valid element

joshua@laptop ~ % mcalc NaCl
Found molecule 'NaCl' in cache
#####

joshua@laptop ~ % mcalc ()
#####

```

## Resources ##
Students are invited to use one of these versions of the Periodic Table.
1. Periodic Table (full table as of #####)
2. Periodic Table (simp[lified table contianing only single-letter elements])

In addition, a sample molecule cache file is included here.