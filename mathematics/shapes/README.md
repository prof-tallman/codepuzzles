# Shape Calculator #
A circle is centered inside a square, as shown in the picture. Compute the area of the square, the area of the circle, and the area of the shaded region between them. The square circumscribes a circle of radius $r$ (so the square's side is $2 \times r$).

## Rankings ##
These stages are friendly suggestions to help new programmers. Skilled students are allowed to complete the project in any order; and they might find better ways to solve the requirements.

1. ***AI Does My HW***:  
   Write a function that returns the area of a square and a circle using radius $r$.
   - Hardcode the radius $r$.
   - Square Area = $4 \times r \times r$.
   - Circle Area = $\pi \times r^2$.
   - Print the area the circle and square, rounded to 3 decimals.

2. ***Script Kiddie***:  
   Calculate the area of an n-sided polygon in addition to the circle and square.
   - Create an algorithm to determine the area of a polygon with an arbitrary number of sides.
     - The circle should circumscribe the polygon.
     - Write the algorithm as a function that takes two inputs $r$ and $n$ and returns the area.
     - Hardcode the number of sides for the polygon $n$ and the radius $r$.
   - Print out the area of the circle, square, and the n-sided polygon.

3. ***Professional***:  
   Let the user choose the parameters and use them to calculate the shaded difference between the square and circle/polygon.
   - Read $r$ (radius) and $n$ (sides) from the command line.
   - If parameter $n$ is omitted, use the circle area instead of the polygon area.
   - Validate: $r > 0$ (float) and $n$, if it exists, $n >= 3$ (integer).
   - By default, only output the shaded area to 3 decimals.
   - Add a flag `--explain` that will also print: square area, circle/polygon area, and the formula used.
   - If any errors occur, graceful end the program with a helpful message.

4. ***1337 H@cker***:  
   Add a drawing mode that will show the square, n-sided polygon, and shaded area.
   - When the user includes the flag `--draw`, use a graphics library to draw the shapes.
   - Output the shaded area to 3 decimals by printing it to STDOUT.

5. ***BONUS***:  
   

## AI Restrictions ##
Students are allowed to use AI LLMs such as ChatGPT to look up basic language features (e.g., how to parse command-line args, compute sine/tangent, or round numbers).

However, students are prohibited from giving the AI any information about the project. If the AI guesses the context and provides sample code, please ignore it. Basically, students may use AI as a convenient interface to official documentation but may not use AI to write any of the project.

## Constraints ##
Additional assumptions and constraints are listed below.
- Most programming languages use radians for trigonometric functions.
- Round printed numbers to 3 decimals.
- The polygon is regular and centered; the square is centered on the same point.

## Examples ##
In the first example, the radius has been hardcoded to 5. In the second, the radius was hardcoded to 5 and the number of sides to 6.
```
user@computer:~$ python shapes.py
Square: 100
Circle: 78.540

user@computer:~$ python shapes.py
Square:  100
Circle:  78.540
Polygon: 64.952

user@computer:~$ python shapes.py 5
21.460

user@computer:~$ python shapes.py 5 --explain
21.460
Area of Square:  100
Area of Circle:  78.540
Formula: Area of Square - Area of Circle
         4 * r^2 - π * r^2

user@computer:~$ python shapes.py 5 6
35.048

user@computer:~$ python shapes.py 5 6 --explain
35.048
Area of Square:  100
Area of Polygon: 64.952
Formula: Area of Square - Area of Polygon
         4 * r^2 - n * r^2 * sin(π/n) * cos(π/n)

user@computer:~$ python shapes.py 5 6 --explain
35.048
Area of Square:  100
Area of Polygon: 64.952
Formula: Area of Square - Area of Polygon
         4 * r^2 - n * r^2 * sin(π/n) * cos(π/n)
```

## Resources ##
Most students won't have too much difficulty calculating the area of squares and circles. However, the algorithm to calculate the area of an n-sided polygon is probably a fair amount more difficult.