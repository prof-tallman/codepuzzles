# Save Me The Money Amortization Table #
Create a program that calculates and displays an amortization table for a loan.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Display a summary of the loan parameters.
   - Calculate and print out the default monthly payment.
   - Also include the interest portion and principal portion for the first payment.
   - Hardcode the loan parameters: total borrowed, APR (%), and loan term (number of months).

2. ***Script Kiddie***:  
   Create and display an amortization table.
   - The amortization table must contain one row for every month in the loan.
   - List the payment number, the payment amount, the interest amount, the principal portion, and the remaining balance.
   - Only print the first five entries from the amortization table.
   - Continue to use hardcoded loan parameters.

3. ***Professional***:  
   The full amortization table is too long to display on the screen; save it to a text file, instead.
   - Save the full table to a text file, one month per line
   - Print the details for the first five payments and the last five payments to the screen.
   - Print a set of elipses (`...`) or some other delimeter between the first five and the last five payments so that it is obvious that some entries have been omitted.
   - Continue to use hardcoded parameters.

4. ***1337 H@cker***:  
   Turn this little utility into a full command line program.
   - Instead of using hardcoded parameters, take command line aguments for the total borrowed, APR, and the loan term.
   - In addition to printing the first and last five rows of the amortization table, also print the total amount paid in interest.

5. ***BONUS***:  
   Add an optional fourth parameter that allows the user to specify an extra monthly payment. Assume that the same extra payment will be made every month for the life of the loan.

## AI Restrictions ##
Students may use AI to look up:
- How to parse command-line arguments (e.g., argparse)
- Number formatting (rounding, commas) and printing tables
- File I/O basics (read/write text or CSV)

Students may not share this full project text or ask AI to write the entire solution. Use AI only as a quick reference to documentation for individual functions and syntax.

## Constraints ##
Perform all calculations manually using loops and the payment formula. Finance libraries are prohibited.
- Round currency values to 2 decimals for display; keep higher precision internally to reduce rounding drift.
- Handle edge cases:
  - Zero APR: monthly payment is simply principal / months; interest is always 0.
  - Tiny remaining balance in the last row: clamp to zero and adjust the last payment.
  - Invalid inputs (negative or zero principal/term, negative APR): print a clear error and exit.
- Output must be human-readable with labels and units ($), aligned columns.
- When writing to a file, include a header row with column names.

## Examples ##
*Numbers shown are illustrative; output will differ based on inputs.*
```
user@computer:~$ python loan.py 
Loan: $25,000.00  APR: 6.00%  Term: 60 months
Monthly payment:     $483.32
Month 1: interest = $125.00, principal = $358.32

user@computer:~$ python loan.py 
Loan: $25,000.00  APR: 6.00%  Term: 60 months
Monthly payment:     $483.32
#   Payment    Interest   Principal   Balance
0     0.00       0.00       0.00      25,000.00
1   483.32     125.00     358.32      24,641.68
2   483.32     123.21     360.11      24,281.57
3   483.32     121.41     361.91      23,919.66
4   483.32     119.60     363.72      23,555.94
5   483.32     117.78     365.54      23,190.40

user@computer:~$ python loan.py
Wrote 60 rows to amortization.csv 
Loan: $25,000.00  APR: 6.00%  Term: 60 months
Monthly payment:     $483.32
#   Payment    Interest   Principal   Balance
0     0.00       0.00       0.00      25,000.00
1   483.32     125.00     358.32      24,641.68
2   483.32     123.21     360.11      24,281.57
3   483.32     121.41     361.91      23,919.66
4   483.32     119.60     363.72      23,555.94
5   483.32     117.78     365.54      23,190.40
    ...
56  483.32      23.03     460.29       1,817.03
57  483.32      18.17     465.15       1,351.88
58  483.32      13.52     469.80         882.08
59  483.32       8.82     474.50         407.58
60  483.32       4.08     479.24           0.00

user@computer:~$ python loan.py 
Wrote 60 rows to amortization.csv
Loan: $25,000.00  APR: 6.00%  Term: 60 months
Monthly payment:     $483.32
#   Payment    Interest   Principal   Balance
0     0.00       0.00       0.00      25,000.00
1   483.32     125.00     358.32      24,641.68
2   483.32     123.21     360.11      24,281.57
3   483.32     121.41     361.91      23,919.66
4   483.32     119.60     363.72      23,555.94
5   483.32     117.78     365.54      23,190.40
    ...
56  483.32      23.03     460.29       1,817.03
57  483.32      18.17     465.15       1,351.88
58  483.32      13.52     469.80         882.08
59  483.32       8.82     474.50         407.58
60  483.32       4.08     479.24           0.00
Total interest paid: $4,999.20
```

## Resources ##
Wikipedia has some helpful resources dealing with mortgage payments, such as the [Equated Monthly Installment](https://en.wikipedia.org/wiki/Equated_monthly_installment) and [Mortgage Calculator](https://en.wikipedia.org/wiki/Mortgage_calculator) pages. See also this [online calculator](https://www.calculator.net/amortization-calculator.html) that can be used to verify the accuracy of a calculation.