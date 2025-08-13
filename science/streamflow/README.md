# Streamflow Analyzer #
Analyze a three-week dataset of streamflow measurements from a U.S. Geological Survey (USGS) NWIS station. Instead of pulling live data, you’ll work with a CSV file that already contains the data dump. You’ll manually parse and process this file, calculate summary statistics, and eventually create a plot.

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
   - Convert that column's values from strings to numbers as you process the rows.
   - Manually compute (avoid any pre-existing statistics function for you):
     - Minimum value
     - Maximum value
     - Mean value (rounded to 0 decimal places)
     - Range of values
   - Print the results in a readable format.

3. ***Professional***:  
   Output important streamflow statistics that help scientists understand the health of the ecosystem.
   - Print the start and end date for the flow measurements.
   - Calculate the total volume of water that has flowed past the sensor over the last 10 days in acre-feet
   - Extrapolate the river's change in flow over the last hour using the most recent two discharge measurements, report the rate in cfs/hour. Always report a positive number, but explain whether the river is rising or dropping.
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
- How to parse strings into integers or floats
- Unit conversions and statistical algorithms
- How to format numbers or strings for printing
- How to use common graph/plot libraries (for the final stage)

Students may not share the project description or ask AI to write the complete solution. Asking the AI to connect individual concepts is also prohibited.

## Constraints ##
This project has a number of important details that must be followed.
- All numeric calculations for stages 1–4 must be done manually, by manually iterating over dataset. No statistics or data-analysis libraries are allowed (but rest assured, they exist... if you need to do this outside of the classroom).
- Dates in the CSV file will be in YYYY-MM-DD format.
- The discharge column contains numeric values in cubic feet per second (cfs).
- Discharge readings are reported every 15 minutes, an important fact for several of the calculations.
- Output should be human-readable, show units, and be neatly aligned.
- Use common plotting libraries to handle all graphics (but no additional analysis libraries). A common module for Python is called Matplotlib.

## Examples ##
Here are some sample runs for a ***different*** dataset than what has been provided to you.
```
user@computer:~$ python streamflow.py
2025-01-01 00:00 -> 8010 CFS
2025-01-01 00:15 -> 8200 CFS
2025-01-01 00:30 -> 8150 CFS
2025-01-01 00:45 -> 8050 CFS
2025-01-01 01:00 -> 7980 CFS

user@computer:~$ python streamflow.py
Discharge statistics:
Min:   3260 CFS
Max:   14300 CFS
Mean:  5251 CFS
Range: 11040 CFS

user@computer:~$ python streamflow.py streamflow.csv
Streamflow from 2025-01-01 00:00 to 2025-02-28 23:59
  Min:   3260 CFS
  Max:   14300 CFS
  Mean:  5251 CFS
  Range: 11040 CFS
Over the past 10 days, 104,152 acre-feet have flowed down the river
The river is currently at 9540 CFS and rising at 20 CFS/hr
```

## Resources ##
Streamflow dataset to use for this project: [streamflow.csv](https://github.com/prof-tallman/codepuzzles/tree/main/science/streamflowstreamflow.csv). The data for this project originally came from US Geological Survey (USGS) [National Water Information System](https://waterdata.usgs.gov/nwis) (NWIS) databases. The data can be [downloaded again](https://waterservices.usgs.gov/nwis/iv/?sites=11530000&startDT=2019-05-01&endDT=2019-06-30&parameterCd=00060&siteStatus=all&format=json) here, but students will need to reformat it from JSON to CSV format.
