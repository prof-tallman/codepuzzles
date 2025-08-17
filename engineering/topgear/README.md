# Top Gear #
Build a Raspberry Pi–based device that rides in a car, collections motion data, and provides the driver with a trip report. This device will be based data collected from an onboard accelerometer and gyroscope.

**WARNING: This project has not been tested yet and is subject to change.**

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Read values from the accelerometer and gyroscope sensors.
   - Connect the accelerometer and gyroscope sensors.
   - Install and configure Raspberry Pi OS.
   - Write functions that collect data from the two sensors.
   - Print out the first 10 sets of readings in a readable format.

2. ***Script Kiddie***:  
   Record driving dynamics to a CSV file.
   - Choose a name for the logfile that is based on the date and time so that multiple runs do not overwrite the original file.
   - Log timestamped acceleration and rotation readings once per second.
   - Store the result in a CSV file with header: datetime, ax, ay, az, gx, gy, gz.
   - After 30 seconds of logging, stop and close the file.

3. ***Professional***:  
   Create a second program that computes summary statistics from a recorded trip.
   - Second program can run on the Raspberry Pi or any other computer.
   - Read the CSV file into the second program that stores the data as a list of tuples.
   - Calculate:
     - Maximum forward acceleration (m/s²)
     - Maximum braking deceleration (m/s²)
     - Maximum lateral acceleration (cornering force, m/s²)
     - Maximum yaw rate (deg/s)
   - Print results with clear labels.
   Take a few test runs in a car and review the results. Choose threshold values that differentiate between 'grandma' driving, 'normal' driving, and 'insane' driving.
   - Print a snarky editorial comment at the end of each ride.

4. ***1337 H@cker***:  
   Plot driving dynamics from a trip.
   - Increase the samplping rate to 10 Hz.
   - Use a graphing library to plot forward acceleration, lateral acceleration, and yaw rate vs time.
   - Label axes and add a title.
   - Save the figure as `topgear.png`.

5. ***BONUS***:  
   Incorporate an additional sensor with the Raspberry Pi device. Examples:
   - Use a magnetometer to show heading changes during the trip.
   - Use the barometer to estimate elevation change while driving.
   - ???

## Constraints ##
A few constraints to keep in mind:
- Sampling rate: 1 Hz (once per second) for initial stages.
- All statistics for stages 1–3 must be calculated manually with loops.
- CSV files must be human-readable and neatly formatted.
- All plots must be clear, labeled, and uncluttered.
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
Datasheets for Raspberry Pi sensors will be coming soon.