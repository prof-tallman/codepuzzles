# Currency Exchange #
Create a currency exchange calculator.

You’ll start with a hardcoded dictionary of exchange rates, then load rates from a file, add command-line arguments, and finally handle fees, formatting, and simple multi-step conversions.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Write a function that converts US Dollars to another currency using an exchange rate dictionary.
   - Create a rates dictionary that holds the exchange rate for a 4-5 different currencies. The keys are currency names (abbreviations) and the values are currency rates.
   - Define the dictionary as value per $1.00 USD (e.g., `{"GBP": 0.75, "EUR": 0.85, "YEN": 155}`)
   - In the function, compute `converted = usd_amount * rates[target]`
   - Then call the fuction with a hardcoded dollar amounts, new currency types, and the exchange rate dictionary.
   - Print the results.
   ```
   user@computer:~$ python currency.py
   25.00 USD -> 21.25 EUR  (rate 0.85 per USD)
   ```

2. ***Script Kiddie***:  
   Load the exchange rate dictionary from a text file.
   - A sample text file is provided (one entry per line in `CURRENCY:value` format).
   - Open the file, read all lines, strip whitespace, skip blanks and lines starting with #, and split on the `:` character.
   - Validate that codes are all-caps letters and values parse as floats.
   - Build rates (a dictionary) and then run the hardcoded conversions as in the previous stage.
   ```
   user@computer:~$ python currency.py
   Using currency file: 'rates.txt'
   25.00 USD -> 21.25 EUR  (rate 0.85 per USD)
   25.00 USD -> 18.75 GBP  (rate 0.75 per USD)
   25.00 USD -> 3875.00 YEN  (rate 155.00 per USD)
   ```
   
3. ***Professional***:  
   Turn it into a command-line tool.
   - Positional parameters: `<target_code> <usd_amount>` (e.g., EUR 25.00).
   - Optional flag: `--rates PATH` to point to a specific rates file (default to `rates.txt` in the current directory).
   - Do not let the code crash. If errors are detected, exit gracefully. Errors might be for an unknown currency code, a missing file, or an invalid number.
   - Output a tidy one-line result (rounded to 2 decimals) and a second line that echoes the rate used.
   ```
   user@computer:~$ python currency.py gbp 10
   10.00 USD -> 7.50 GBP
   (rate used: 0.75 GBP per USD; source: rates.txt)

   $user@computer:~$ python currency.py EUR 25 --rates my_rates.txt
   25.00 USD -> 21.25 EUR
   (rate used: 0.85 per USD; source: my_rates.txt)
   ```

4. ***1337 H@cker***:
   Read the rates file from an online source and add some real-world details.
   - If the `--rates` flag is omitted, instead of reading from a local file, download the exchange rates from an internet server (it could be this very Github server).
   - Fees/Spread: support `--fee-pct X` to model a transaction fee (e.g., 2.5%). The new computation will be `net = usd_amount * (1 - X/100)` before conversion.
   - Batch mode: accept multiple amounts: `EUR 10 25 100` → print one line per amount.
   - Pretty formatting: optional `--precision N` (default 2) and `--symbol` to print currency symbol if known, otherwise do not use a symbol (e.g.: $, €, £, ¥).
   ```
   user@computer:~$ python currency.py eur 100 250 --fee-pct 2.5
   Source: https://raw.githubusercontent.com/prof-tallman/codepuzzles/refs/heads/main/finance/currency/rates.txt
   Rate used is 0.85 GBP per USD
   100.00 USD ->  82.87 EUR  (2.5% fee)
   250.00 USD -> 207.18 EUR  (2.5% fee)

   user@computer:~$ python currency.py --fee-pct 2.5 --symbol eur 100 250 
   Source: https://raw.githubusercontent.com/prof-tallman/codepuzzles/refs/heads/main/finance/currency/rates.txt
   Rate used is 0.85 GBP per USD
   100.00 $ ->  82.87 €  (2.5% fee)
   250.00 $ -> 207.18 €  (2.5% fee)

   user@computer:~$ python currency.py RUB 10
   Source: https://raw.githubusercontent.com/prof-tallman/codepuzzles/refs/heads/main/finance/currency/rates.txt
   Error: currency code 'RUB' not found in rates file.
   Run with --list to see available codes.

   user@computer:~$ python currency.py --list --rates rates.txt
   Source: rates.txt
   Available rates (per 1 USD):
     EUR :   0.85
     GBP :   0.75
     YEN : 155.00
     ...
   ```   

5. ***BONUS***:
  **WARNING: this stage is likely to change**
  Convert from any currency to any other, not just USD→target.
  - A comprehensive rates file is provided; each entry is still “value per 1 USD.”
  - For SRC→DST, compute:
    $$
    amount_dst=amount_src \times \dfrac{rate[SRC]}{rate[DST]​}
    $$
  - New CLI form: `--from SRC --to DST AMOUNT [--rates PATH] [--fee-pct X]`.

## AI Restrictions ##
Students may use AI to look up:
- How to open and read text files
- How to parse strings into numbers and split lines
- Basic command-line parsing or string formatting
- How to download a file from an online source
- Other basic programming concepts

Students may not share the project text or ask AI to write the complete solution. Do not ask AI to assemble the whole program; limit questions to individual language features.

## Constraints ##
Additional constraint are listed below:
- All parsing and calculations must be performed manually with built-in data types. No external data-analysis libraries are allowed.
- Exchange rate file format: one entry per line as `CODE:value` (e.g., `EUR:1.05`). Lines may include blanks and # comments; ignore both.
- Currency codes are case-insensitive on input but should be stored/printed uppercase.
- Rounding: default to 2 decimal places for outputs unless `--precision` is provided.
- Helpful errors and graceful exits are always required
- For the first three stages, do not fetch live rates; use local text files.

## Resources ##
Two resources will come in handy for this project:
- [ISO 4217 currency codes](https://en.wikipedia.org/wiki/ISO_4217) (for 3-letter codes)
- Sample [rates.txt](https://raw.githubusercontent.com/prof-tallman/codepuzzles/refs/heads/main/finance/currency/rates.txt) file. Copy locally for stages 2-3 but change your program to download the file directly from the server for stage 4.
