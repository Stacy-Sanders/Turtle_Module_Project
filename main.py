from turtle import Turtle, Screen, colormode
from random import choice, randint
# import turtle as t
# tator = t.Turtle()

tator = Turtle()
tator.shape("turtle")
tator.color("darkTurquoise")
no_sides = 0

colors = ["red", "blue", "green", "yellow", "black", "purple", "orange", "NavyBlue", "LightSlateBlue", "brown",
          "orchid", "PaleGreen", "firebrick", "honeydew4", "gold", "GhostWhite", "ForestGreen", "blue4", "aquamarine"]
directions = [0, 90, 180, 270]  # set heading ie [east, north, west, south]


def square(turtle):
    for i in range(4):
        turtle.right(90)
        turtle.fd(100)


# square(tator)

# tator.left(90)


def dashed_line(turtle):
    for i in range(15):
        turtle.fd(10)
        turtle.pu()
        turtle.fd(10)
        turtle.pd()


# dashed_line(tator)


def shape(turtle, sides):
    angle = 360 / sides
    for i in range(sides):
        turtle.fd(100)
        turtle.right(angle)


def all_shapes(turtle):
    turtle.right(90)
    for i in range(3, 11):
        turtle.color(choice(colors))
        shape(turtle, i)


def random_walk(turtle):
    turtle.pensize(15)
    turtle.speed("fastest")
    for i in range(200):
        turtle.color(choice(colors))
        turtle.fd(30)
        turtle.setheading(choice(directions))


# random_walk(tator)
# Turtle shows up better at tend - change to white
# tator.color("white")

colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb_colors = (r, g, b)
    return rgb_colors


def random_walk2(turtle):
    turtle.pensize(15)
    turtle.speed("fastest")
    for i in range(200):
        turtle.color(random_color())
        turtle.fd(30)
        turtle.setheading(choice(directions))


# random_walk2(tator)


def spirograph(turtle):
    pass


def spiral(turtle, size_of_gap):
    circ = 360 / size_of_gap
    turtle.speed("fastest")
    for i in range(int(circ)):
        turtle.color(random_color())
        turtle.circle(50)
        turtle.setheading(turtle.heading() + size_of_gap)


spiral(tator, 10)
spiral(tator, 5)
screen = Screen()
screen.exitonclick()
