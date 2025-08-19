# Periodic Table Lookup #
Write a program that will calculate the molecular mass of a molecule like "H2O".

The molecule should be written using standard chemical notation with uppercase and lowercase letters that specifies each individual element and the number of atoms that it contains. For example, water would be given as "H2O" and salt would be input as "NaCl".

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Write code to parse a molecule string and print the individual elements and their quantities.
   - Iterate through the molecule, printing out each element or quantity, one per line.
   - Restrict the molecule to single-letter elements like `H2O`.
   - For now, students are allowed to ignore molecules such as "NaCl" that contain atoms identified by multiple letters.
   - The internal periodic table can be stored as a data file or hardcoded directly into the program.
   - Call this function with a few hardcoded molecules to demonstrate that it works.
   ```
   user@computer:~$ python madchemist.py
   Parsing molecule 'H2O'
     element H
     quantity 2
     element O
   Parsing molecule 'CPO3H'
     element C
     element P
     element O
     quantity 3
     element H
   ```

2. ***Script Kiddie***:
   Calculate the overall mass of the molecule.
   - Sum the weights of the individual elements and print out the result.
   Allow users to choose their own molecules with a commnad line parameter.
   - The program must accept the molecule as a positional command line parameter.
   - Users should input single-letter molecules like `O2` or `H2O`.
   - Instead of printing each elements and quantities on separate lines, print each element and quantity together
   - If a number is missing, it implies that the quantity is 1
   ```
   user@computer:~$ python madchemist.py H2O
   Parsing molecule 'H2O'
     H x 2
     O x 1
     H2O has a mass of 18.015
   ```
   
3. ***Professional***:
   Improve the parsing code so that the program recognizes any/all elements from the periodic table.
   - The full periodic table file contains single-letter elements and the multi-letter elements.
   - All elements begin with an upper-case letter.
   - If the element requires multiple letters then all of the subsequent letters will be lower-case.
   - Handle invalid elements with a helpful error message.
   Read the periodic table from a text file
   - Use an optional command line argument `--ptable FILE` to specify a custom periodic table file
   - If `--ptable` is missing, use a default periodic table file
   - This allows users to update the periodic table if a new element is discovered.
   ```
   user@computer:~$ python madchemist.py NaCl
   Parsing molecule 'NaCl'
     Na x 1
     Cl x 1
     NaCl has a mass of 58.44

   user@computer:~$ python madchemist.py Na3PO4
   Parsing molecule 'Na3PO4'
     Na x 3
     P x 1
     O x 4
     Na3PO4 has a mass of 163.94

   user@computer:~$ python madchemist.py Nz3PO4
   Parsing molecule 'NzQb2'
     Error: element 'Nz' could not be found in the periodic table.

   user@computer:~$ python madchemist.py Nz3PO4 --ptable future_ptable.txt
   Parsing molecule 'NzQb2'
     Nz x 1
     Qb x 2
     NzQb2 has a mass of 593.62
   ```

4. ***1337 H@cker***:  
   Add a caching feature that will save the molecular formula and mass of any/all inputs to a text file.
   - Every time that a new molecule is processed--a molecule that is not already included in the cache--the mass will be calculated manually and then the result will be saved to the cache. 
   - But before taking the time to run the slow manual calculation, the program should check the cache and, if the molecule exists in the cache, use the cached answer instead of performing the calculation from scratch.
   - If the program finds a molecule in the cache, it should include a short message explaining this in the output.
   ```
   user@computer:~$ python madchemist.py NaCl
   Parsing molecule 'NaCl'
     Na x 1
     Cl x 1
     NaCl has a mass of 58.44

   user@computer:~$ python madchemist.py NaCl
   Found 'NaCl' in the moleculular cache
   NaCl has a mass of 58.44
   ```

5. ***BONUS***:  
   Modify the program to handle nested "submolecules" such as Aluminium Sulfate Al2(SO4)3.
   - The submolecule, in this case SO4, is enclosed in parenthesis with a number immediately following it. This means that the molecule includes three PO4 submolecules.
   - The proper chemistry term for these submolecules is a *polyatomic ion* or, perhaps, *polyatomic group* for those who are not chemistry experts.
   ```
   user@computer:~$ python madchemist.py Al2(SO4)3
   Parsing molecule 'Al2(SO4)3'
     Al x 2
     S x 1
     O x 4
     SO4 x 3
     Al2(SO4)3 has a mass of 342.132
   ```

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
If a molecule specifies any elements that are not part the provided periodic table, the program should detect this error, print an error message, and exit gracefully.

Students with a chemistry background will be aware that there are physical properties at the atomic level that restrict arbitrary combinations of atoms from forming molecules; for example, there's no such thing as NOCFe2. Validating the chemical validity of a given molecule is **not** required. Students are encouraged to simply read the individual elements and sum their masses, regardless of whether the elements form an actual molecule.

## Resources ##
Students are invited to use one of these versions of the Periodic Table.
1. [Periodic Table](https://github.com/prof-tallman/codepuzzles/blob/main/science/periodic_table/periodic_table.txt) (the full table as of December 2024)
2. [Periodic Table Singletons](https://github.com/prof-tallman/codepuzzles/blob/main/science/periodic_table/periodic_table_singletons.txt) (a simplified version of the table contianing only single-letter elements)

In addition, a sample moleculular cache file is included [here](https://github.com/prof-tallman/codepuzzles/blob/main/science/periodic_table/molecule_cache.txt).
