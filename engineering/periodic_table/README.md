# Periodic Table Lookup #
Write a program that will calculate the molecular mass of a molecule.

The molecule should be written using standard chemical notation with uppercase and lowercase letters that specifies each individual element and the number of atoms that it contains. For example, water would be given as "H2O" and salt would be input as "NaCl".

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Write a function that will parse a molecule string and print the individual elements and their quantities.
   - Restrict the molecule to single-letter elements like `H2O` (students are allowed to ignore molecules such as "NaCl" that contain atoms identified by multiple letters).
   - The periodic table used by the program for lookups may either be provided as a hardcoded table or as a data file.
   - Call this function with a few hardcoded modules to demonstrate that it works.

2. ***Script Kiddie***:
   Allow users to choose their own molecules with commnad line parameters.
   - The program must accept a command line parameters, it cannot rely on input functions in the code such as `input` (Python), `ReadLine` (C#), or `gets` (C).
   - Users may input single-letter molecules like `O2` or `H2O`

3. ***Professional***:
   Improve the molecule parsing function so that it understands and properly calculates the mass of any/all elements in the periodic table. Read the periodic table file dynamically at runtime.
   - The larger periodic table file is complete; it contains the single-letter elements and the multi-letter elements.
   - All elements begin with an upper-case letter; if the symbol requires multiple letters then all of the subsequent letters will be lower-case.
   - Read the periodic table from a text file every time the program runs so that it will be able to handle new, as of yet undiscovered elements simply by updating the periodic table text file.

4. ***1337 H@cker***:  
   Add a caching feature that will save the molecular formula and mass of any/all inputs to a text file.
   - Every time that a new molecule is input--e.g., a molecule that is not already included in the cache--it will be calculated manually using your code and then the result will be saved to the cache. 
   - Before taking the time to run the slow manual calculation, the program should check the cache and, if the molecule exists in the cache, use the cached answer instead of running the calculation from scratch.
   - If the program finds a molecule in the cache, it should include a short message explaining this in the output.

5. ***BONUS***:  
   Modify the program to handle nested "submolecules" such as Barium Phosphate Ba3(PO4)2.
   - The submolecule, in this case PO4, is enclosed in parenthesis with a number immediately following it. This means that the molecule includes two PO4 submolecules.
   - The proper chemistry term for these submolecules is a *polyatomic ion* or, perhaps, *polyatomic group* for those who are not chemistry experts.

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

Students with a chemistry background will be aware that there are physical properties at the atomic level that restrict arbitrary combinations of atoms from forming molecules; for example, there's no such thing as NOCFe2. Validating the chemical validity of a given molecule is **not** required. Students are encouraged to simply read the individual elements and sum their masses, regardless of whether the elements form an actual molecule.

## Examples ##
```
user@computer:~$ mcalc H2O
#####

user@computer:~$ mcalc ASDFG
Error: molecule 'A' is not a valid element

joshua@laptop:~$ mcalc NaCl
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