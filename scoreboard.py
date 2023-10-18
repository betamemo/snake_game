from turtle import Turtle

FONT = ('verdana', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()  # hide an arrow
        self.score = 0
        self.highest_score = 0
        self.print_highest_score()

    def print_score(self):
        self.goto(280, 260)
        self.write(f'Score: {self.score}', align='right', font=FONT)

    def print_highest_score(self):
        self.goto(-280, 260)
        self.write(f'Highest Score: {self.highest_score}', align='left', font=FONT)

    def add_score(self, score):
        self.score += score
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=FONT)
