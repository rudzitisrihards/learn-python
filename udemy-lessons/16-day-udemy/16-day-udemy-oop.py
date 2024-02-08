# class = blueprint for object
# object = has some attributes (variables) and methods (functions)

# object = ClassName()

# import turtle
# timmy = turtle.Turtle()

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

timmy.shape("turtle")
timmy.color("coral")
timmy.shapesize(stretch_wid=2)
timmy.forward(100)

my_screen = Screen()

my_screen.exitonclick()