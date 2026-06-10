import turtle

# Activity 1 - Draw Square
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)

# Activity 2 - Draw Triangle
for i in range(3):
    t.forward(100)
    t.left(120)

# Activity 3 - Draw Circle
t.circle(50)

turtle.done()