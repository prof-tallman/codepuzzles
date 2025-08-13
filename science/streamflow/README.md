# Streamflow Analyzer #
Analyze a three-week dataset of streamflow measurements from a U.S. Geological Survey (USGS) NWIS station. Instead of pulling live data, you’ll work with a CSV file that already contains the data dump. You’ll manually parse and process this file, calculate summary statistics, and eventually create a plot — but without using Pandas or Numpy until after the project is complete.

The dataset contains daily measurements for parameters such as discharge, gauge height, and possibly temperature. All calculations in the first stages must be done manually by iterating through a list of lists after parsing the CSV file.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students may complete the project in any order and might find better ways to meet the requirements.

1. ***AI Does My HW***:  
   Read a CSV file and print the first few data rows.
   - The CSV will have a header row and then one row per daily observation.
   - Open the file, read all lines, strip whitespace, and split each row on commas.
   - Store the result in a list of lists (data), where each sub-list represents one row.
   - Print the first 5 rows (not including the header) to confirm parsing worked.

2. ***Script Kiddie***:  
   Extract and print basic statistics for the discharge column.
   - Identify the column index for discharge from the header row.
   - Convert that column's values from strings to floats as you process the rows.
   - Manually compute (avoid any pre-existing statistics function for you):
     - Minimum value
     - Maximum value
     - Mean value
     - Range of values
   - Print the results in a readable format.

3. ***Professional***:  
   Output important streamflow statistics that help scientists understand the health of the ecosystem.
   - Calculate the total volume of water that has flowed past the sensor over the last 10 days in acre-feet
   - Extrapolate the river's change in flow over the last hour using the most recent two discharge measurements, report the rate in cfs/hour.
   - Use position-based command line parameters to specify the name of the file. Assume that any files provided by the user will follow the same structure/format as the sample file.

4. ***1337 H@cker***:  
   Plot a graph that shows the streamflow over the time period contained in the file.
   - Add a title and label the axis appropriately
   - Scale the axis for the data in the file (most graphing libraries will do this automatically)
   - Avoid cluttering the graph with unnecessary features
   - Save the plot as discharge.png in the current directory

5. ***BONUS***:  
   Predicts the streamflow for the next week using linear regression.
   - Manually calculate the line for the linear regression
   - Plot the linear regression for 3 days into the future.

## AI Restriction ##
Students may use AI to look up:
- How to open and read CSV files
- How to parse strings into floats
- Unit conversions and statistical algorithms
- How to format numbers or strings for printing
- How to use Matplotlib for plotting (only at the final stage)

Students may not share the project description or ask AI to write the complete solution. Asking the AI to connect individual concepts is also prohibited.

## Constraints ##
This project has a number of important details that must be followed.
- All numeric calculations for stages 1–4 must be done manually, by manually iterating over dataset. No statistics or data-analysis libraries are allowed (but rest assured, they exist... if you need to do this outside of the classroom).
- Dates in the CSV file will be in YYYY-MM-DD format.
- The discharge column will have numeric values in cubic feet per second (cfs).
- Discharge readings are reported every 15 minutes, an important fact for several of the calculations.
- Output should be human-readable, show units, and be neatly aligned.
- Use common plotting libraries to handle all graphics (but no additional analysis libraries). A common module for Python is called Matplotlib.

## Examples ##
```
user@computer:~$ python streamflow.py data.csv
['2024-07-01', '2.12', '3.45', '...']
['2024-07-02', '2.56', '3.67', '...']
['2024-07-03', '2.48', '3.22', '...']
['2024-07-04', '2.75', '3.55', '...']
['2024-07-05', '2.98', '3.78', '...']

user@computer:~$ python streamflow.py data.csv
Discharge statistics:
Count: 21
Min: 2.12 cfs
Max: 3.78 cfs
Mean: 2.94 cfs
```

## Resources ##
The data for this project came from US Geological Survey (USGS) [National Water Information System](https://waterdata.usgs.gov/nwis) (NWIS) databases.
