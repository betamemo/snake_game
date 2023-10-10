from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

positions = [(0, 0), (20, 0), (40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        for p in positions:
            new_snake = self.create_snake(p)
            self.segments.append(new_snake)
        self.head = self.segments[-1]

    def create_snake(self, position):
        new_snake = Turtle()
        new_snake.shape('square')
        new_snake.color('lightgreen')
        new_snake.penup()
        new_snake.goto(position)
        return new_snake

    def go_up(self):
        self.head.setheading(UP)
        # self.head.forward(10)

    def go_down(self):
        self.head.setheading(DOWN)
        # self.head.forward(10)

    def go_left(self):
        self.head.setheading(LEFT)
        # self.head.forward(10)

    def go_right(self):
        self.head.setheading(RIGHT)
        # self.head.forward(10)

    def move(self):
        # for s in self.segments:
        #     s.forward(20)
        for i in range(len(self.segments) - 1):
            curr = self.segments[i]
            next = self.segments[i+1]
            curr.goto(next.pos())
        self.head.forward(20)