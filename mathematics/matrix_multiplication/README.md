# Matrix Multiplication #
Write a program that multiplies two matrices together.

A matrix is a rectangular arrangement of numbers in rows and columns. In order to multiply two matrices:
- The number of columns in the first matrix must equal the number of rows in the second matrix.
- If the first matrix is $m \times n$ and the second is $n \times k$, the resulting matrix will be $m \times k$.
- The element at position $(i,j)$ in the result is found by:
  - Taking the i-th row from the first matrix and the j-th column from the second matrix.
  - Multiplying each pair of corresponding elements.
  - Adding up all those products (this is the dot product of the row and column).

For example, multiplying a $2 \times 3$ matrix by a $3 \times 2$ matrix:
$\begin{bmatrix}1 & 2 & 3 \\\ 4 & 5 & 6\end{bmatrix} \times \begin{bmatrix} 7 & 8 \\\ 9 & 10 \\\ 11 & 12\end{bmatrix}=$

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.
1. ***AI Does My HW***:  
   Multiply two hardcoded matrices and print the result.
   - Write a function `matrix_multiply(A, B)` that:
     - Accepts two matrices represented as lists of lists.
     - Returns a new matrix containing the result of multiplying $A \times B$.
   - In main, call this function with two hardcoded matrices that meet the multiplication dimension requirement.
   - Print the resulting matrix in a readable format (rows on separate lines).

2. ***Script Kiddie***:  
   Let the user enter the matrix values.
   - Ask the user for the dimensions of each matrix ($m \times n$ and $n \times k$).
   - Prompt for the values of each matrix row by row.
   - Validate that the first matrix's column count matches the second matrix's row count; if not, print an error and quit gracefully.
   - Print the result in a clean, labeled format.

3. ***Professional***:  
   Load matrices from files.
   - Accept two filenames as command line arguments; read each file into a matrix (rows separated by newlines, values separated by spaces or commas).
   - Validate that the files contain numeric data and that dimensions match the multiplication rule.

4. ***1337 H@cker***:  
   Create two new options that improve the user experienc.
   - Add an optional `--pretty` flag to format output in aligned columns.
   - Add an optional `--transpose` flag to automatically transpose the second matrix before multiplication. What this means is that your program will be able to multiple matrices with dimensions $m \times n$ and $k \times n$ if, and only if, the `--transpose` flag is used because it will convert the second matrix to a new matrix of dimension $n \times k$.

5. ***BONUS***:  
   Add advanced benchmarking functionality and performance checks.
   - Implement a `--random m n k min max` option that:
     - Generates an m × n matrix and an n × k matrix.
     - Fills them with random integers between min and max.
   - Detect and warn if the result contains numbers that exceed a certain threshold (e.g., 1,000,000). When this occurs, give the user the option to quit or continue as early as possible.
   - Measure and print the time taken for each multiplication.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to look up basic features and examples within the programming language. For example, someone might ask how to split a string into numbers, read from a file, or format text into aligned columns.

However, students are prohibited from giving the AI any information about the project. If the AI guesses the context and provides sample code, please ignore it. Basically, students may use AI as a convenient interface to official documentation but may not use AI to write any of the project.

## Constraints ##
Additional assumptions and constraints are listed below:
- Matrix multiplication modules such as Python's Numpy, the C# Matrix class, and Java's EJML are prohibited. Students must manually perform all indexing and multiplication. 
- Only numeric data is supported (integers or floats).
- Round floating-point results to 3 decimals when printing.
- Validate all inputs (user or file) and provide helpful error messages.
- Large random matrices may take noticeable time to compute, so handle with care.

## Examples ##
The first example is for the "AI Does My Homework" stage and uses an internal, hardcoded matrix. The second example is for the "Script Kiddie" which prompts the user to dynamically enter their own matrix. The last example (forth) shows pretty printing.
```
user@computer:~$ python matrix.py
[58, 64]
[139, 154]

user@computer:~$ python matrix.py
Enter rows and columns for first matrix: 2 3
Enter first matrix row 1: 1 2 3
Enter first matrix row 2: 4 5 6
Enter rows and columns for second matrix: 3 2
Enter second matrix row 1: 7 8
Enter second matrix row 2: 9 10
Enter second matrix row 3: 11 12
Result:
[58, 64]
[139, 154]

user@computer:~$ python matrix.py matrix1.txt matrix2.txt
[58, 64]
[139, 154]

user@computer:~$ python matrix.py matrix1.txt matrix2.txt --pretty
  58   64
 139  154
```

## Resources ##
Additional resources are not required for this project.