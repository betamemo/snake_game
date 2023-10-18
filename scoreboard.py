from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()  # hide an arrow

    def print_score(self):
        self.goto(0, 260)
        self.write(f'Score: {self.score}', align='center', font=('Arial', 25, 'normal'))

    def add_score(self, score):
        self.score += score
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=('Arial', 40, 'normal'))
