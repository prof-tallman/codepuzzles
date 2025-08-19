# Top Gear #
Build a portable motion-sensing device that rides in a car, records data from its motion sensors, and generates a simple trip report for the driver. This device can run a Raspberry Pi and incorporates sensors such as an accelerometer and gyroscope.

**WARNING: This project has not been tested yet and is subject to change.**

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Read values from the accelerometer and gyroscope sensors.
   - Connect the accelerometer and gyroscope sensors to the Raspberry Pi.
   - Install and configure the Raspberry Pi software.
   - Write functions to collect data from the two motion sensors.
   - Create a simple test that prints the first 10 sets of readings.

2. ***Script Kiddie***:  
   Record the driving motion to a log file.
   - Instead of printing the sensor readings to the screen, save them to a log file.
   - The name of the logfile should be based on the current date and time to avoid name collisions.
   - Collect a new measurement from the two sensors every second.
   - Each line should contain a timestamp in addition to the accelerometer and gyroscope readings.
   - Store the result in a text file using the column headers: `datetime`, `ax`, `ay`, `az`, `gx`, `gy`, `gz`.
   - After 30 seconds of logging, stop and close the file.

4. ***Professional***:  
   Create a second program that computes summary statistics from a recorded trip.
   - This second program reads the log files created by the first program.
   - The second program can run on the Raspberry Pi sensor or on another computer; it just needs a log file.
   - Read every line from log file and store the data as a list of tuples.
   - From the data (e.g., the list of tuples), calculate:
     - Maximum forward acceleration (m/s²)
     - Maximum braking deceleration (m/s²)
     - Maximum lateral acceleration (cornering force, m/s²)
     - Maximum yaw rate (deg/s)
   - Print results with clear labels.
   Rate the driver based on the measurements.
   - Take a few test runs in a car and review the results.
   - Try driving slow-and-steady, medium, and then fast-jerky.
   - Based on the readings, choose threshold values that differentiate between 'grandma' driving, 'normal' driving, and 'insane' driving.
   - The program should print snarky comments based on these categories.

6. ***1337 H@cker***:  
   Plot the driving motion from each trip.
   - Increase the samplping rate from 1 Hz to 10 Hz.
   - Use a graphing library to creat three plots: forward acceleration, lateral acceleration, and yaw rate vs time.
   - Label the axes and add a title.
   - Save the figure as `topgear.png`.

7. ***BONUS***:  
   Incorporate an additional sensor with the Raspberry Pi device. Examples:
   - Use a magnetometer to show heading changes during the trip.
   - Use the barometer to estimate elevation change while driving.
   - ???

## Constraints ##
A few constraints to keep in mind:
- Sampling rate: 1 Hz (once per second) for initial stages and 10 Hz later on.
- All statistics for stages 1–3 must be calculated manually with loops.
- Log files must be human-readable and neatly formatted.
- The plots must be clear, labeled, and uncluttered.
- Errors should be detected and handled gracefully.

## Examples ##
```
user@pi:~$ python tgcollect.py
2025-10-14 15:31:04 Accelerometer (m/s²): X=0.12, Y=0.05, Z=0.03   Gyroscope (deg/s): X=0.03, Y=0.01, Z=0.15
2025-10-14 15:31:05 Accelerometer (m/s²): X=0.10, Y=0.06, Z=0.04   Gyroscope (deg/s): X=0.03, Y=0.01, Z=0.15
... (8 more rows) ...

user@pi:~$ python tgcollect.py
2025-10-14 16:44:55 Accelerometer (m/s²): X=0.12, Y=0.05, Z=0.03   Gyroscope (deg/s): X=0.03, Y=0.01, Z=0.15
2025-10-14 16:44:56 Accelerometer (m/s²): X=0.10, Y=0.06, Z=0.04   Gyroscope (deg/s): X=0.03, Y=0.01, Z=0.15
... (8 more rows) ...
Data saved to 'topgear_20251014_164524.csv'

user@pi:~$ python tgreport.py topgear_20251014_164524.csv
Trip statistics:
  Max accel forward:   2.8 m/s²
  Max brake force:    -3.4 m/s²
  Max cornering force: 2.1 m/s²
  Max yaw rate:       40.3 deg/s
```

## Resources ##
Datasheets for the Raspberry Pi sensors will be coming soon.
