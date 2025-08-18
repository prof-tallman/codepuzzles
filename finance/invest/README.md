# Retirement Account #
Simulate the year-by-year growth of a retirement account invested in a single fund. Assume a long-term average growth rate, but add a small random variation each year so returns aren’t identical. The program will generate an annual table showing contributions, yearly return, gain/loss, and balance.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Display a summary of the investment parameters and compute the first year.
   - Hardcode the investment parameters:
     - `initial_balance` (e.g., $10,000)
     - `annual_contribution` (e.g., $6,000, paid at end of each year)
     - `growth_rate` (e.g., 7.0 for 7% per year)
     - `volatility` (e.g., 2.0 means ±2.0, so each year’s rate is drawn uniformly from [5%, 9%])
     - `years` (e.g., 30)
   - Randomly generate the actual growth within [expected_rate_pct ± variability_pct].
   - Compute and print a performance statement for the first year:
     - start balance
     - applied rate (%)
     - gain/loss (start × rate)
     - contribution (end-of-year)
     - end balance

2. ***Script Kiddie***:  
   Create and display an annual table.
   - One row per year for `years` years with columns:
     - `Year`, `Rate%`, `Gain/Loss`, `Contribution`, `End of Year Balance`
   - Use the same randomization rule for each year (independent number per year).
   - Print the first 5 rows only (keep using hardcoded parameters).

3. ***Professional***:  
   Save the full table to a file; print a front/back preview.
   - Write all rows to `retirement.csv` (one year per line; include a header).
   - On screen, print the first 5 rows and the last 5 rows.
   - Print `...` between the two blocks so it’s obvious that some rows were omitted (first-5 vs last-5).- After the table preview, print summary metrics:
     - Total contributions (sum of yearly contributions)
     - Total investment gain/loss (final balance − total contributions − initial balance)
     - Average growth rate
     - Final balance

4. ***1337 H@cker***:  
   Add a simple Monte Carlo mode to simulate multiple years and aggregate the results.
   - New flag: `--mc RUNS` to run multiple independent simulations (e.g., 100).
   - Collect the final balances across runs and report:
     - Minimum, median (50th percentile), and 90th percentile final balances
     - Probability of reaching a user goal if `--goal AMOUNT` is provided
   - If Monte Carlo mode is used, do not print any individual tables because it would clutter the screen. Just print the summary results at the end.

5. ***BONUS***:  
   Turn your little program into a full command-line tool.
   - Use positional arguments to specify the investment parameters (accept integers/floats):
     - `initial_balance`
     - `annual_contribution`
     - `expected_rate` (accept either 0.07 or 7.0; detect and normalize)
     - `volatility` (± band; accept 0.02 or 2.0; detect and normalize)
     - `years`
   - Optional flags (note: students must implement all of these flags but the user has the option to use them):
     `--seed S` set the RNG seed for reproducible runs
     `--out FILE` path for CSV output (default is `retirement.csv`)
     `--top N` only print the first N lines (still write the full CSV)
     `--no-commas` print numbers without thousands separators
   Validate all inputs and quit gracefully with an error message if there any errors.
   Reuse the same logic as earlier stages and print the same summary metrics.

## AI Restrictions ##
Students may use AI to look up:
- How to parse command-line arguments
- Number formatting (rounding, commas) and printing tables
- File I/O basics (read/write CSV)
- Random number generation (distribution functions, seeding)
- Other general information about the programming language of choice

Students may not share this full project text or ask AI to write the entire solution. Use AI only as a quick reference to documentation for individual functions and syntax.

## Constraints ##
Algebra only; use loops and simple arithmetic. No financial or statistics libraries. Remember, the purpose of these projects are to learn fundamental programming skills.
Annual compounding model (define clearly and use consistently):
- Contribution timing: contribution is added at end of year after applying that year’s rate to the starting balance.
```
gain = start * rate
end  = start + gain + contribution
```
To calculate the random growth rate per year, generate a random number from a uniform range [expected_rate − variability, expected_rate + variability].
Accept both decimal (0.07) and percent (7.0) inputs; normalize to decimal internally.
Do not allow rates outside ±50%.
Rounding:
- Round printed money values to 2 decimals; keep higher precision internally.
Generate clear, human-readable console output with labels and units ($), aligned columns.
Print helpful messages if any error occurs.

## Examples ##
*Numbers shown are illustrative; output will differ based on inputs.*
```
user@computer:~$ python invest.py 
Initial balance: $10,000.00
Annual contribution (end-of-year): $6,000.00
Expected rate: 7.00% ± 2.00%
Horizon: 30 years

Year 1:
  Start:  $10,000.00
  Rate:     8.24%
  Gain:   $   824.00
  Contrib:$ 6,000.00
  End:    $16,824.00

user@computer:~$ python invest.py 
Year  Rate%   Gain/Loss  Contrib   End
0        -           -          -  10,000.00
1     8.24      824.00   6,000.00  16,824.00
2     6.31    1,061.59   6,000.00  23,885.59
3     9.01    2,150.08   6,000.00  32,035.67
4     5.44    1,742.74   6,000.00  39,778.41
5     6.52    2,592.63   6,000.00  48,371.04

user@computer:~$ python invest.py 
Wrote 30 rows to retirement.csv
Year  Rate%   Gain/Loss  Contrib   End
0        -           -         -   10,000.00
1     8.24      824.00  6,000.00   16,824.00
2     6.31    1,061.59  6,000.00   23,885.59
3     9.01    2,150.08  6,000.00   32,035.67
4     5.44    1,742.74  6,000.00   39,778.41
5     6.52    2,592.63  6,000.00   48,371.04
    ...
26    8.67   28,117.16  6,000.00   358,235.93
27    5.83   20,895.37  6,000.00   385,131.30
28    6.11   23,528.52  6,000.00   414,659.82
29    7.93   32,880.07  6,000.00   453,539.89
30    4.76   21,572.56  6,000.00   481,112.45

Totals:
  Contributions:   $180,000.00
  Investment gain: $291,112.45
  Final balance:   $471,112.45
```

## Resources ##
No special resources are required for this project.