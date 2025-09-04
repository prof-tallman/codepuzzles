# Stock Trader #
Analyze a three-week dataset [stocks.csv](https://github.com/prof-tallman/codepuzzles/tree/main/finance/stock_tracker/stocks.csv) of stock price bars from a single ticker (e.g., 15-minute closes) in a CSV file. Parse and process the data to calculate summary statistics, generate a report, and create a plot.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Read a CSV file and print the first few rows of data.
   - The CSV will have a header row and then one row per time interval.
   - Open the file, read all lines, split each row on commas, and strip any whitespace.
   - Store the result in a list of tuples (`data`), where each tuple represents one row.
   - Print the first 5 rows and the header, to confirm that the parsing code worked.
   ```
   user@computer:~$ python stocks.py
   2025-04-01 09:30 -> $174.12, Vol 128,450
   2025-04-01 09:45 -> $174.65, Vol 96,210
   2025-04-01 10:00 -> $174.22, Vol 84,005
   2025-04-01 10:15 -> $175.10, Vol 110,392
   2025-04-01 10:30 -> $175.48, Vol 89,771
   ```

2. ***Script Kiddie***:  
   Extract and print basic statistics for the `Price` column.
   - Every power reading is given in USD and is the closing price for the interval.
   - Read every row and convert the `Price` values from strings to numbers.
   - Manually compute some basic statistics, avoiding any pre-existing statistics modules:
     - Minimum value
     - Maximum value
     - Mean value (rounded to 2 decimals)
     - Range of values
   - Print the results in a readable format.
   ```
   user@computer:~$ python stocks.py
   Price statistics:
   Min:    $168.03
   Max:    $177.92
   Mean:   $173.46
   Range:  $9.89
   ```

4. ***Professional***:  
   Generate a trading summary to help understand recent market activity.
   - Print the start and end timestamp for the dataset.
   - Using the most recent 10 calendar days found in the file:
     - Sum the total share volume (`Volume`) over those days.
     - Compute total dollar volume by summing `Price × Volume` for each row.
   - Estimate the price change rate from the last two rows:
     - Report as dollars per hour (use the actual time delta between those two rows and then scale number up to "dollars per hour").
     - Always print a positive rate and state whether price is rising or falling (or holding stead).
   - Use a position-based command line parameter to specify the CSV filename. Assume that future files follow the same structure.
   ```
   user@computer:~$ python stocks.py prices.csv
   Price data from 2025-04-01 09:30 to 2025-04-19 16:00
     Min:    $168.03
     Max:    $177.92
     Mean:   $173.46
     Range:  $9.89
   Last 10 days:
     Total volume:      42,318,955 shares
     Total $ volume:    $7,321,445,812
   Current price is $175.12 and increasing at $2.40 per hour
   ```

5. ***1337 H@cker***:  
   Plot a graph that shows the price over the time period contained in the file.
   - Add a descriptive title with the ticker symbol and date range, and label axes (time vs. price in USD).
   - Let the graphing library auto-scale axes; avoid clutter (no 3D, no unnecessary gridlines).
   - Save the plot as `price.png` in the current directory.

6. ***BONUS***:  
   Predict the price trend for the next day using linear regression.
   - Manually compute a best-fit line $y = m \times x + b$ for the last N data points (choose N, e.g., the last 2–3 days of bars).
   - Plot the regression line and extend it one trading day into the future (same bar spacing as the CSV).
   - Draw a vertical dashed line separating historical data from the forecast.

## AI Restrictions ##
Students may use AI to look up:
- How to open and read CSV files
- How to parse strings into integers or floats
- Basic statistical formulas and unit conversions
- How to format numbers/strings for printing
- How to use common plotting libraries (for the final stage)

Students may not share the project description or ask AI to write the complete solution. Asking AI to connect multiple steps into a full solution is also prohibited.

## Constraints ##
This project has a number of important details that must be followed.
- All numeric calculations for stages 1–4 must be written manually by iterating over the dataset. No statistics or data-analysis libraries.
- Datetime values in the CSV use the format `YYYY-MM-DD HH:MM` (24-hour time).
- The CSV contains at least these columns:
  - `Datetime` — bar time
  - `Price` — close price for the interval (USD)
  - `Volume` — shares traded during the interval (integer)
- Prices are recorded every 15 minutes during trading hours (assume this interval for any rate calculations).
- For the "last 10 days" calculations, treat "days" as the last 10 distinct calendar dates present in the data.
- Output should be human-readable, show units, and be neatly aligned.
- Use a common plotting library for graphics (e.g., Matplotlib); do not use additional analysis libraries.

## Examples ##
```
user@computer:~$ python stocks.py
2025-04-01 09:30 -> $174.12, Vol 128,450
2025-04-01 09:45 -> $174.65, Vol 96,210
2025-04-01 10:00 -> $174.22, Vol 84,005
2025-04-01 10:15 -> $175.10, Vol 110,392
2025-04-01 10:30 -> $175.48, Vol 89,771

user@computer:~$ python stocks.py
Price statistics:
Min:    $168.03
Max:    $177.92
Mean:   $173.46
Range:  $9.89

user@computer:~$ python stocks.py prices.csv
Price data from 2025-04-01 09:30 to 2025-04-19 16:00
  Min:    $168.03
  Max:    $177.92
  Mean:   $173.46
  Range:  $9.89
Last 10 days:
  Total volume:      42,318,955 shares
  Total $ volume:    $7,321,445,812
Current price is $175.12 and increasing at $2.40 per hour
```

## Resources ##
