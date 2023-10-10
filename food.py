import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('img/apple.gif')
        self.penup()
        self.food_pos()

    def food_pos(self):
        self.goto(random.randint(-300, 300), random.randint(-300, 300))
