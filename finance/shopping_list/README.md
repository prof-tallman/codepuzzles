# Shopping List Tax Calculator #
Create a program that will read a shopping list from a file, calculate the tax, and show the final receipt.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***: 
   Compute the total cost of a shopping list using three parallel arrays: names, prices, and a Boolean "taxable" flag. Apply a single, customizable sales-tax rate to taxable items only.
   - Hardcode three arrays of equal length:
   - `items = [ ... ]` (strings)
   - `prices = [ ... ]` (numbers)
   - `taxable = [ ... ]` (booleans: `True` if sales tax applies, `False` otherwise)
   - Also hardcode a tax rate (e.g., `tax_rate = 0.0825` for 8.25%).
   Loop through the three parallel lists to calculate and print the total price.

2. ***Script Kiddie***:
   Print a receipt summary with: subtotal (pre-tax), tax amount, and grand total.
   - Add a fourth parallel array for the quantity of each item; e.g., `counts = [...]`.
   - For each item, print the name, price, quantity, and whether tax was applied.
   - Round money to 2 decimals for display, but keep higher precision internally to reduce rounding drift.
   - At the end, print the total base price, the total tax, and the overall total.
   - Continue using a hardcoded shopping list and tax rate.

3. ***Professional***:
   Make the program configurable from the command line.
   - Positional arg: `tax_rate RATE` (as a percentage like 8.25 or a decimal like 0.0825; accept both, determine which one the user provided, and normalize).
   - Optional flags:
     - `--top N` → print only the first N line items (for long lists), still compute full totals.
     - When using the `--top N` flag, print the most expensive N line items
     - `--no-commas` → print numbers without thousands separators (by default, large numbers should be printed with commas separating every three digits).
   - Validate that the arrays are the same length; on mismatch, print a helpful error and exit gracefully.

4. ***1337 H@cker***:
   Combine the shopping list with a store inventory to create a simple e-commerce capability.
   Instead of relying on hardcoded arrays, the shopping list comes from a CSV file on disk. And it's not so much a shopping list, but more of a store inventory and price list.
   - The CSV file should contain four columns: item `name`, `price`, `taxable`, and `count`.
   - `count` contains the number of items in stock at the store, not the customer's desired quantity.
   - Parse the file line-by-line, ignoring blank lines and any line starting with #.
   - If an invalid entry is found, skip that line and continue, but print a warning.
   Use a second CSV file to represent the shopping list.
   - The shopping list file should just include the item names and a quantity.
   - Customers can only purchase items that the store has in stock.
   - If the name of a requested item does not match the name of an item sold by the store, the customer cannot buy the item.
   Add a command-line option `--inventory PATH` and `--list PATH` to specify the store inventory and the shopping list CSV to load (default to shopping.csv if not provided).
   Print the same nicely formatted receipt, but now sourced entirely from the two CSV files.
   - Make a special note when if a requested item cannot be fulfilled.

5. ***BONUS***:
   Turn the program into an e-commerce website. Build a small HTTP server that serves prices from a server-side inventory CSV and accepts a shopping cart via POST to compute totals.

## AI Restrictions ##
Students may use AI to look up:
- How to parse command line arguments (argparse)
- String/number conversion and formatting
- Reading simple CSV files
- Other basic concepts in the programming language of choice

However, students may not share this project text or ask AI to write a partial solution. Use AI as a quick reference for specific syntax only.

## Constraints ##
- Use parallel arrays or a list of dictionaries.
- Do all calculations with loops and simple arithmetic—no data-analysis libraries.
- Treat `tax_rate` as uniform and consistent across all taxable items.
- Round all printed results to 2 decimals but keep a higher-precision running total internally.
- Validate all inputs: e.g., non-negative prices; booleans parsed from true/false/1/0 (case-insensitive).
- Output must be human-readable, labeled, and neatly aligned.
- When reading CSV, trim whitespace; ignore blank lines and comment lines starting with #

## Examples ##
```
user@computer:~$ python shopping.py 
Tax rate: 8.25%
Subtotal:    $116.47
Tax:           $6.68
Total:       $123.15

user@computer:~$ python shopping.py 
Items:
1) Notebook          1x  $  4.99   taxable: no
2) Headphones        1x  $ 29.95   taxable: yes
3) Apples (3 lb)     1x  $  5.37   taxable: no
4) USB-C Charger     3x  $ 24.50   taxable: yes
5) Office Chair      1x  $ 51.66   taxable: yes

Tax rate: 8.25%
Subtotal:    $165.47
Tax:          $13.65
Total:       $179.12

user@computer:~$ python shopping.py tax_rate 5.0 --top 3
Items:
1) USB-C Charger     3x  $ 24.50   taxable: yes
2) Office Chair      1x  $ 51.66   taxable: yes
3) Headphones        1x  $ 29.95   taxable: yes
...

Tax rate: 5.25%
Subtotal:    $165.47
Tax:           $8.27
Total:       $173.74
```

## Resources ##
There are no special resources required for this project.