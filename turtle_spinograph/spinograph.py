import turtle as t
import random

shape = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
shape.speed(5)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        shape.color(random_color())
        shape.circle(100, steps=10) #defining the shape with steps
        shape.setheading(shape.heading() + size_of_gap)

draw_spirograph(5)


