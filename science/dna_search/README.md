# DNA Search #
Search DNA sequences for a nucleotide sequence and return the surrounding context (±k nucleotides). Start with a hardcoded string, then add command-line arguments, file/FASTA support, approximate matching, and directory mode.

DNA strings use the alphabet `A`, `C`, `G`, `T`. Unless otherwise specified, treat inputs case-insensitively and normalize to uppercase internally.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students may complete the project in any order and might find better ways to meet the requirements.

1. ***AI Does My HW***:  
   Search a DNA sequence for a particular nucleotide sequence and print the first occurence and the context around it.
   - Write `dna_search(seq, query, k)` that returns the first occurence of `query` in `seq`.
     Each match is `(start_index, context)`, where
     `context = seq[start_index - k) : start_index + len(query) + k]`.
   - Avoid indexing errors for matches at the very beginning or very end of a sequence.
   - Normalize both `seq` and `query` to uppercase; reject sequences or queries with non-ACGT nucleotides.
   - In main, call the function with hardcoded values (e.g., k=5) and verify output.

2. ***Script Kiddie***:  
   Turn the DNA search function into a small command line program.
   - Change the `dna_search` function to return a list of all matches.
   - Use positional command line parameters to specify the `sequence` and `query`. Provide an optional `-k/--context N` parameter to let the user choose a value for `k` (default value is `k=5`).
   - Add a `--count` flag to print the total number of matches but to omit the actual results.
   - For each match, print the starting index and context in a way that all the queries are aligned and easy to see.
   - Handle empty input and invalid characters gracefully.

3. ***Professional***:  
   Add new features including reading the genome sequence from a file.
   - `--file <path>` reads the sequence from a text file. By default, each line is an independent sequence.
     - For the output, display the filename and line number in addition to the index and context
     - Line numbers should be 1-based (e.g. the first line is line #1) and indices are 0-based
   - `--join` treats the whole file as one long sequence, even if there are multiple lines. Remove any whitespace between the sub-sequences, whether it is due to newline characters, spaces, or tabs.
   - `--max N`: caps the maximum number of printed matches.
   - Allow overlapping matches. For example, if the sequence was `ACGTACGTAC` and the query `ACGTAC`, there would be two matches. The last two letters of the first match would overlap with the first two letters of the second match.

4. ***1337 H@cker***:  
   Support common biological formats and output the results to a file.
   - Allow for both DNA and RNA nucleotide sequences. In RNA, the nucleotide `U` (Uracil) replaces `T` (Thymine).
   - Add a new flag `--fasta` that works in conjunction with `--file <path>`. When the `--fasta` flag is used, the input file are assumed to be in the FASTA file format.
   - If the `--output <path>` flag is used, the results should be stored in a CSV file.
     - The CSV file should include 6 columns: filename, line number, index, previous-k nucleotides, match string, and next-k nucleotides. The context has been split across three columns.
   - Manually search through the input sequence rather than relying on search functions provided by the programming language.

5. ***BONUS***:  
   Add new features as interested/appropriate:
   - Provide an approximation search in addition to the previous exact search.
     - `--hamming D` allows ≤ D mismatches for equal-length query windows.
     - Include the mismatch count in the output when used.
   - Directory mode: `--dir PATH` scans `*.fa`, `*.fasta`, and `*.txt` (optionally --recursive) and runs the same search/report on each file. Handle missing/unreadable files gracefully; continue processing others.
   - Compression: auto-detect `.gz` inputs for files/FASTA.

## AI Restriction ##
Students may use AI LLMs to look up how to: parse command-line arguments, read files, parse FASTA, implement Hamming distance, or handle `.gz` files.

Students may not share the project text or ask AI to write the solution. Treat AI like a searchable interface to official documentation and language references only.

## Constraints ##
Please see the following constraints:
- Accept mixed case input but internally normalize all output to uppercase.
- Validate all input with the DNA alphabet: `A`, `C`, `G`, `T` (and sometimes `U`). Any other character in sequence or query is an error (except FASTA header lines starting with > when --fasta).
- Context window: if the match is near the start/end, pad the output with whitespace placeholders so that all of the output matches line up.
- Do not crash, even when there are errors. Instead, produce clear, actionable messages for things like invalid alphabets, empty input, and missing files.

## Examples ##
```
user@computer:~$ python dnalookup.py "AGTAGTCGTTGTTGTCA" "GTT" -k 4
7   ...AGTC [GTT] GTTG...
10  ...CGTT [GTT] GTCA

user@computer:~$ python dnalookup.py "AGTAGTCGTTGTTGTCA" "AAA" --count
0

user@computer:~$ cat seqs.txt
AGTA
GTCGTTG
GTTTCA
user@computer:~$ python dnalookup.py --file seqs.txt GTT -k 2
seqs.txt 2:3  ...TC [GTT] G
seqs.txt 3:0        [GTT] TC...

user@computer:~$ cat genes.fasta
>geneA
AGTAGTCG
TTGTTG
>geneB
cgat
user@computer:~$ python dnalookup.py --fasta --file genes.fasta GTT -k 2
geneA 2:2  ...TG [GTT] G
```

## Resources ##
Students working with FASTA data will need to lookup the [FASTA format primer](https://www.ncbi.nlm.nih.gov/genbank/fastaformat/). The basic idea is that headers begin with > and sequences follow on subsequent lines. If the FASTA file contains any optinal modifiers after the nucleotide sequence, retain this information (unchanged) in the output.