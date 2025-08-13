# DNA Reverse Complement #
Compute the reverse complement of a DNA sequence. A DNA string uses the letters `A`, `C`, `G`, and `T`. Base-pair complements are `A ↔ T` and `C ↔ G`. The reverse complement is formed by reversing the string and then replacing each base with its complement.

Example: `CGTTTA` → reverse = `ATTTGC` → complement = `TAAACG`.

You’ll start with a hardcoded function and progress to a robust command-line tool that supports files, FASTA, GC content, RNA output, and more.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Write a function that computes the reverse complement of a hardcoded DNA sequence.
   - The function takes a DNA string (letters A, C, G, T only).
   - Reverse the string, then complement each base: `A ↔ T`, `C ↔ G`.
   - Return the reverse complement string.
   - Call the function with a hardcoded test case and print the result.

2. ***Script Kiddie***:  
   Let the user input their own DNA sequence via the command line.
   - Accept mixed case; output must be uppercase.
   - Validate that the sequence contains only `A`, `C`, `G`, `T`.
   - If invalid characters are found, print a helpful error message and exit.

3. ***Professional***:  
   Add command line flags for flexible input and output.
   - `--file <name>`: read DNA from a text file (if this flag is omitted, read from the command line).
     - By default, process the entire file as one long sequence. Remove any vertical or horizontal whitespace so that the output is one long sequence of characters `A`, `C`, `G`, and `T`.
   - `--out <name>`: writes the reverse complement to a file instead of printing (if this flag is omitted, print the result to stdout).
   - `--mseq`: when used with `--file`, process multiple sequences from the file. Treat each line of input in the file as a unique DNA sequence to be reversed and complemented.
   - Handle all file errors gracefully (missing file, unreadable file, or empty input).

4. ***1337 H@cker***:  
   Add biological data features for realism using additional command line parameters.
   - `--gc`: also print the GC content (%) of the input sequence (rounded; see Constraints).
   - `--rna`: output the reverse complement RNA (use `U` instead of `T` in the final output).
   - Support FASTA input (ignore header lines that start with >).
     - When `--mseq` is used with FASTA, treat each header and the following lines (until the next header) as a single sequence record.

5. ***BONUS***:  
   Add `--palindrome` to check if the input sequence is a DNA palindrome (its reverse complement equals the original sequence). Print a clear yes/no line in addition to the normal output.

## AI Restriction ##
Students may use AI LLMs (e.g., to look up how to parse command-line arguments, how to read a file, what a FASTA file looks like, or string/collection methods).

Students may not share the project text or context with AI or ask AI to write the solution. Treat AI like a searchable interface to official documentation and language references only.

## Constraints ##
There are a number of important constraints for this project.
- Accept input sequences with mixed case but treat input case-insensitively; output must be uppercase.
- Valid characters are `A`, `C`, `G`, and `T` only. Ignore spaces, newlines, and tab characters (no errors, just skip over them). All other characters produce errors.
- The GC% content is computed as: $$GC = 100 \times \dfrac{ total G's + total C's}{total nucleotides}$$
- Round displayed GC% to 3 decimals.
- With `--mseq`, output one result per record, in the same order as input.

## Examples ##
The first example shows the "AI Does My HW" stage where the input sequence is hardcoded. In this case, the original sample would have been `CGTTTA`
```
user@computer:~$ python revcomp.py
TAAACG

user@computer:~$ python revcomp.py "cGtttA"
TAAACG

user@computer:~$ cat seqs.txt
AGTAGTCGTTGTTGTCA
ACGTT
user@computer:~$ python revcomp.py --file seqs.txt
AACGTTGACAACAACGACTACT

user@computer:~$ cat seqs.txt
AGTAGTCGTTGTTGTCA
ACGTT
user@computer:~$ python revcomp.py --file seqs.txt --mseq
TGACAACAACGACTACT
AACGT

user@computer:~$ cat genes.fasta
>geneA
AGTA
GT
>geneB
cgat
user@computer:~$ python revcomp.py --file genes.fasta --mseq
>geneA 
ACTACT
>geneB
ATCG

user@computer:~$ python revcomp.py "AGTAGTCGTTGTTGTCA" --gc
TGACAACAACGACTACT
GC% = 44.444

user@computer:~$ python revcomp.py "AGTA" --rna
UACU

user@computer:~$ python revcomp.py "ACGTNX"
Error: invalid character(s) found in sequence: N, X

user@computer:~$ python revcomp.py --file missing.txt
Error: file 'missing.txt' was not found

user@computer:~$ python revcomp.py --file empty.txt
Error: no sequence data found in input file 'empty.txt'
```

## Resources ##
Students working on the 1337 H@cker level will need to lookup the [FASTA format primer](https://www.ncbi.nlm.nih.gov/genbank/fastaformat/). The basic idea is that headers begin with > and sequences follow on subsequent lines. If the FASTA file contains any optinal modifiers after the nucleotide sequence, retain this information (unchanged) in the output.