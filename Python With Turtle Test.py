#Copyright ® 2018 Aymaan Shaikh
#Please Contact Before Using Code

import turtle
import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
turtle.speed(10)
turtle.speed()
#BaseData
#---------------------------------------------------------
alex=turtle.Turtle()
alex.speed(10)
alex = turtle.Turtle()      # create a turtle named alex
alex.forward(150)           # tell alex to move forward by 150 units
alex.left(90)               # turn by 90 degrees
alex.forward(75)            # complete the second side of a rectangle
#--------------------------------------------------------
tess = turtle.Turtle()
tess.speed(10)
import turtle
wn.bgcolor("lightgreen")        # set the window background color


tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(3)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
#---------------------------------------------------------
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
#---------------------------------------------------------
turtle.speed(10)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("green")

tess.penup()                # This is new
size = 20
for i in range(30):
   tess.stamp()             # Leave an impression on the canvas
   size = size + 3          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.right(24)           #  ...  and turn her

wn.mainloop()
#---------------------------------------------------------
wn.bgcolor("orange")        # set the window
#---------------------------------------------------------
turtle.left(20)

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

turtle.left(30)

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

turtle.left(40)

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

#---------------------------------------------------------
turtle.position()
(0.30,240.00)
turtle.sety(-10)
def draw_star(size, color):
    angle = 120
    turtle.fillcolor(color)
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()
    return

draw_star(100, "blue")
#---------------------------------------------------------
painter2 = turtle.Turtle()

painter2.pencolor("#32D486")
painter2.forward(30)

painter2.pencolor("#D6305F")
painter2.forward(30)
#---------------------------------------------------------
tina=turtle.Turtle()
tina.shape('turtle')

def make_cake(x=0, y=0):
    tina.penup()
    tina.color('pink')
    tina.goto(x, y)
    tina.pendown()
    tina.begin_fill()
    tina.goto(x + 20, y)
    tina.goto(x + 20, y + 20)
    tina.goto(x - 20, y + 20)
    tina.goto(x - 20, y)
    tina.goto(x, y)  
    tina.end_fill()
    tina.goto(x, y + 20)
    tina.color('yellow')
    tina.goto(x, y + 35)
    tina.goto(x, y + 30)
    tina.color('black')
    tina.goto(x, y + 20)
    tina.penup()
    tina.goto(x, y + 10)

make_cake(0,0)
make_cake(-100,0)
make_cake(100,0)
#---------------------------------------------------------
tina = turtle.Turtle()
tina.shape('turtle')

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

for each_color in colors:
    angle = 360 / len(colors)
    tina.color(each_color)
    tina.circle(40)
    tina.right(angle)
    tina.forward(30)
#---------------------------------------------------------
tina = turtle.Turtle()
tommy = turtle.Turtle()

tina.color('blue')
tommy.color('green')

tina.shape('turtle')
tommy.shape('turtle')

tina.begin_fill()
tina.goto(200,0)
tina.goto(200,-200)
tina.goto(-200,-200)
tina.goto(-200,0)
tina.goto(0,0)
tina.end_fill()

tommy.penup()
tommy.goto(-70,100)
tommy.write("Tina, let's Make a picture together!")
tommy.goto(0,50)
tommy.pendown()

tina.penup()
tina.color('white')
tina.goto(-40,-100)
tina.write("Alright, I'm ready!!")
tina.goto(0,-130)
tina.pendown()
#---------------------------------------------------------
wn.bgcolor("orange")        # set the window
#---------------------------------------------------------
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
#---------------------------------------------------------
wn.bgcolor("yellow")        # set the window
#---------------------------------------------------------
ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()
#---------------------------------------------------------
turtle.speed(10)
spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)
    
turtle.done()
#---------------------------------------------------------
def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "yellow", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()      # Create tess and set some attributes
tess.pensize(3)

size = 20                   # Size of the smallest square
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10        # Increase the size for next time
    tess.forward(10)        # Move tess along a little
    tess.right(18)          #    and give her some turn

wn.mainloop()
#---------------------------------------------------------
