# Tello Drone Flight #
Fly a drone around an obstacle course.

This puzzle requires access to a DJI Tello Talent Drone, or a similar drone that can be flown programmatically using a suitable programming language. Tello Drones can be controlled with a Python library that allows a computer to send basic commands to the drone. 

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.
1. ***AI Does My HW***: Program a drone to fly autonomously through an obstacle course of your own choosing. The course must include *five* manuevers around obstacles that are no more than 3 meters apart and movement in along all three flight axis (x, y, and z). Submit your code and demonstrate your drone successfully flying through the course.
2. ***Script Kiddie***: Program a drone to fly autonomously through an obstacle course of your own choosing. The course must include *ten* manuevers around obstacles that are no more than 2 meters apart from each other and movement along all three flight axis (x, y, and z). Submit your code and demonstrate your drone successfully flying through the course. For the demonstration, an instructor might ask you to modify the obstacle course to verify sufficient understanding of the program.
3. ***Professional***: Create a program that allows you to interactively fly a drone. The program should allow the pilot to takeoff and land, manuever along all three flight axis (x, y, and z), and take a photograph with the drone's camera. You are allowed to use PyGame and/or other libraries that handle raw keyboard input without pressing the <ENTER> button, but this is not required. If anything unexpected happens, your program should immediately land the drone, display a helpful message, and exit gracefully. Submit your code and demonstrate your drone flying to an interesting location, saving a photograph to a file, and then returning. For the demonstration, an instructor might ask you to modify the flight controls to verify sufficient understanding of the program.
4. ***1337 H@cker***: Complete all of the requirements for the ***Professional*** ranking and add new controls to rotate the drone clockwise/CCW and perform flips. Use a GUI framework such as PyGame to process raw keyboard input and display any photographs taken with the drone's camera. This interface must show the drone's current battery level to the user. Submit your code and demonstrate your drone flying to an interesting location that is not accessible to most people (e.g., inspect the roof for leaks), taking a photograph and displaying it on the GUI display, returning, and performing a flip to celebrate.
5. ***BONUS***: Improve your program's GUI interface to show live video from the camera.

## Constraints ##
Students are allowed to use AI LLMs such as ChatGPT to lookup basic help and API usage for modules like djitellopy and pygame. For example, you might ask which PyGame functions configure the size of the display window (it's )or how to display an image to the display window (it's the 'blit' function). Or, you might ask the AI to describe how the '' function works or how to save a file to disk (...). 

However, students are prohibited from giving the AI any information about the assignment or the context of the program that you are writing. Basically, you may use AI as a nice interface to the official documentation but it may not write any of the project for you.

## Examples ##
Here is a screenshot of a fun interface that some senior computer science students quickly put together. This program goes above and beyond what is expected by completing all of the ***1337 H@cker*** requirements, the ***BONUS*** options, and more. Consider it as inspiration for what can be done with a bit more computer science experience.

## Resources ##
For assistance, see the official documentation:
* DJI Tello User Guide,
* DJI Tello Software Development Kit,
* the current release of the `djitellopy` module,
* ...and the approrpriate PyGame documentation.
