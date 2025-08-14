# Tello Drone Flight #
Create a Tx/Rx controller to fly a drone over a WiFi connection.

This puzzle requires access to a DJI Tello Talent Drone, or a similar drone that can be flown programmatically using a suitable programming language. Tello Drones can be controlled with a Python library that allows a computer to send basic commands to the drone.

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Program a drone to takeoff and land according to keyboard presses. 
   - Many programmable drones accept network connections through an onboard WiFi access point.
   - The computer's host firewall will need to allow network communication with the drone.
   - Before taking off, query the drone's battery level. If the drone is below 30% power, instead of taking off, print an error message and quit gracefully.
   - The same key should be used to takeoff and land.
   In addition to submitting the source code, demonstrate a successful flight for the instructor. 

2. ***Script Kiddie***:  
   Add new controller keys to provide movement and rotation along all possible flight axis.
   - Typically movement relies on keyboard buttons that are arranged like the arrow keys (left, right, up, down); for example, `ADWS` or `JLIK`.
   - Most drones allow eight different movements, requiring two sets of keyboard buttons. The movements are typically forward, backward, left, right, up, down, rotate clockwise and rotate counter-clockwise.
   - Use a keyboard input function that responds to every keystroke immediately (as opposed to the input functions that are completed by pressing the <ENTER> button).
   In addition to submitting the source code, demonstrate a successful flight for the instructor. 

3. ***Professional***:  
   Create a program that allows pilots to interactively fly a drone.
   - Game engines such as Python's PyGame are recommended as they provide an ideal combination of graphics/video and raw/live keyboard input.
   - The program should allow the pilot to takeoff and land repeatedly.
   - Use flight control buttons to move and rotate along all of the possible flight axis.
   - If the drone has a camera, provide a live video feed and setup a new button to save a photograph from the drone's camera.
   - If any errors occur, land the drone safely and quit the program gracefully.
   In addition to submitting the source code, submit a photograph taken by the drone and demonstrate a successful flight for the instructor. 

4. ***1337 H@cker***:  
   Improve the drone controller by create a heads-up display (HUD) and other advanced features.
   - Add a readout of the current battery level and altitude.
   - Automatically land the drone if the battery level reaches 15%
   - Design some sort of throttle control that affects how quickly the drone moves.
   Fly to an interesting location that is not accessible to most people (e.g., inspect the roof for leaks), save a photograph, and return to the landing zone. Submit the source code and photograph.

5. ***BONUS***:
   Record live video from the drone's camera.
   - Use a keyboard button to toggle the recording off/on.
   - Automatically save any recorded video to disk.
   - Use the current time as part of the filename to ensure that old videos are not overwritten by new videos.

## Constraints ##
Students are allowed to use AI LLMs such as ChatGPT to lookup basic help and API usage for any non-standard modules. For example, if using PyGame, students might ask which functions configure the size of the display window (it's ) or how to display an image to the display window (it's the 'blit' function). 

However, students are prohibited from giving the AI any information about the assignment or the context of the project. Basically, students may use AI as a nice interface to the official documentation but it may not write any code for the project.

## Examples ##
Here is a screenshot of a fun interface that some senior computer science students quickly put together. This program goes above and beyond what is expected by completing all of the ***1337 H@cker*** requirements, the ***BONUS*** options, and more. Consider it as inspiration for what can be done with a bit more computer science experience.

## Resources ##
For assistance, see the official documentation:
* [DJI Tello User Manual](https://github.com/prof-tallman/HelloRoboMaster/blob/main/RoboMaster_TT_Tello_Talent_User_Manual_en.pdf)
* [DJI Tello Software Development Kit](https://github.com/prof-tallman/HelloRoboMaster/blob/main/Tello_SDK_3.0_User_Guide_en.pdf)
* [Current Github release](https://github.com/damiafuentes/DJITelloPy) of the `djitellopy` module
* [Sample project](https://github.com/prof-tallman/HelloRoboMaster) using `djitellopy` module in Python
