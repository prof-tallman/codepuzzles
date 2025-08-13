# Ideal Gas Law #
Use the Ideal Gas Law $PV=nRT$ to compute the mole count for the air in a room. Start with simple hardcoded calculations, move to command-line inputs with unit conversion, and then integrate Raspberry Pi sensors to read temperature and pressure while estimating room volume. In the Ideal Gas Law, $P \times V = n \times R \times T$, where 𝑃 is pressure ($atm$), 𝑉 is volume ($m^3), 𝑛 is moles of gas, 𝑇 is temperature (K), and 𝑅 is the gas constant.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   On your personal computer, write a function that computes the number of moles $n$ of a gas using hardcoded values for P, V, R, and T.
   - Use $P = 1 atm$ and $R = 8.205736 m^3 \cdot atm \cdot K^{-1} \cdot mol^{-1}$
   - Hardcode a reasonable volume $V$ and temperature $T$ for your dorm room, making sure that you use the correct units.
   - Calculate and print the number of moles $n$ for the room.

2. ***Script Kiddie***:
   Still on your personal computer, modify the program to let the user input command line parameters for the volume of the room.
   - Allow the user to use either `--si` or `--metric` to specify whether the volume measurements are in feet or meters.
   - Use three command line positional arguments to that represent the width, length, and height of a room. If these parameters are missing, assume $10' \times 12' \times 8'$ as the dimensions and print a short message to remind the user of these default dimensions.
   - When necessary, convert the user's input from cubic feet to cubic meters for the calculation.

3. ***Professional***:
   Transfer your program to a Raspberry Pi and run it manually.
   - It would be easiest to run the Raspberry Pi device in graphical desktop mode with a monitor, although students are welcome to try the command line version of Raspberry Pi OS.
   - Every time that the program runs, in addition to printing the output, it should also save the readings and calculations to a log file.
     - Limit the log file entry to a single line. Find a simple, easy to read format for the output.
     - Make sure that each line of the log file contains a timestamp.

4. ***1337 H@cker***:
   Instead of hardcoding physical values, connect the Raspberry Pi to external sensors that will measure the conditions of the room.
   - If possible, use a temperature sensor to measure the current temperature in the room.
   - If possible, use a barometer to measure the air pressure in the room.
   - Take note of the units for the sensor readings and perform unit conversion as necessary.

5. ***BONUS***:
   Connect to the Raspberry Pi over the internet to take remote sensor readings and calculations. Students may connect to Raspberry Pi remotely over SSH and run the code manually or install a simple web server to post periodically post the sensor readings and calculations.

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to look up basic features and examples within the programming language (e.g., how to parsing command-line arguments or read a sensor).

However, students are prohibited from giving the AI any information about the project. If the AI guesses the context and provides sample code, please ignore it. Basically, students may use AI as a convenient interface to official documentation but may not use AI to write any of the project.

## Constraints ##
- Round all output to 3 decimal places.
- Detect common errors and quit gracefully with a helpful error message.

## Examples ##

## Resources ##