import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('images/apple.gif')
        self.penup()
        self.food_pos()

    def food_pos(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
