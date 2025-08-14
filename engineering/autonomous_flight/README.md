# Tello Drone Flight #
Fly a drone around an obstacle course. In this project, students will program the drone to fly autonomously through obstacle courses and create an interactive control system.

This puzzle requires access to a DJI Tello Talent Drone, or a similar drone that can be flown programmatically using a suitable programming language. Tello Drones can be controlled with a Python library that allows a computer to send basic commands to the drone. 

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Program a drone to fly autonomously through an obstacle course of the students own choosing. 
   - The course must include *five* manuevers around obstacles that are no more than three meters apart
   - The course requires movement along *two* of the three flight axis (x, y, and z).
   Submit the source code and demonstrate a successful flight through the course.

2. ***Script Kiddie***:  
   Increase the complexity of the obstacle ocurse.
   - The course must include *ten* manuevers around obstacles that are no more than two meters apart
   - Movement must include *all three* flight axis (x, y, and z).
   Submit the source code and demonstrate a successful flight through the course.

3. ***Professional***:  
   Integrate curved movements to make for a smoother flight around the obstacle course.
   - Not every turn needs to be curved, but students must use at least three different curves
   - Curved functions are difficult and probably require pencil-paper calculations.
   Submit the source code and demonstrate a successful flight through the course.

4. ***1337 H@cker***:  
   Program the drone to fly in a pattern that spells "CSC104".
   - The letters should be drawn vertically in the air so that an observer on the ground can easily watch the movements.
   - Use the curve functions to create smooth letter Cs, Ss, and 0s.
   - Connect the letters from one to another in whatever pattern seems most appropriate.
   - Drones may need to backtrack in order to position themselves for the next letter.
   Submit the source code and demonstrate a successful flight through the course.

5. ***BONUS***:
   Attach a light to the top of the drone so that the drone's movement can be seen at night.

## Constraints ##
Students are allowed to use AI LLMs such as ChatGPT to lookup basic help and API usage for modules such as `djitellopy`. For example, students might ask for help understanding and using the `curve_xyz_speed` function and the difference between `(x1, y1, z1)` vs `(x2, y2, z2)` parameters. 

However, students are prohibited from giving the AI any information about the assignment or the context of the programming project. Basically, students may use AI as a nice interface to the official documentation but it may not write any of the project code.

## Examples ##
Coming soon!

## Resources ##
Most students will be using DJI Tello drones and programming in Python.
* [DJI Tello User Manual](https://github.com/prof-tallman/HelloRoboMaster/blob/main/RoboMaster_TT_Tello_Talent_User_Manual_en.pdf)
* [DJI Tello Software Development Kit](https://github.com/prof-tallman/HelloRoboMaster/blob/main/Tello_SDK_3.0_User_Guide_en.pdf)
* [Current Github release](https://github.com/damiafuentes/DJITelloPy) of the `djitellopy` module
* [Sample project](https://github.com/prof-tallman/HelloRoboMaster) using `djitellopy` module in Python

