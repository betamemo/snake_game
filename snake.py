from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.head = self.create_turtle()

    def create_turtle(self):
        new_turtle = Turtle()
        new_turtle.shape('circle')
        new_turtle.color('lightgreen')
        new_turtle.penup()
        return new_turtle

    def go_up(self):
        self.head.setheading(UP)
        self.head.forward(10)

    def go_down(self):
        self.head.setheading(DOWN)
        self.head.forward(10)

    def go_left(self):
        self.head.setheading(LEFT)
        self.head.forward(10)

    def go_right(self):
        self.head.setheading(RIGHT)
        self.head.forward(10)
