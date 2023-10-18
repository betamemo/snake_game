from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

init_pos = [(0, 0), (20, 0), (40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        for pos in init_pos:
            new_snake = self.create_snake(pos)
            self.segments.append(new_snake)
        self.head = self.segments[-1]

    def create_snake(self, pos):
        new_snake = Turtle()
        new_snake.penup()
        new_snake.shape('square')
        new_snake.color('lightgreen')
        new_snake.goto(pos)
        return new_snake

    def go_up(self):
        self.head.setheading(UP)

    def go_down(self):
        self.head.setheading(DOWN)

    def go_left(self):
        self.head.setheading(LEFT)

    def go_right(self):
        self.head.setheading(RIGHT)

    def move(self):
        for i in range(len(self.segments) - 1):
            curr = self.segments[i]
            next = self.segments[i + 1]
            curr.goto(next.pos())
        self.head.forward(20)

    def extend_snake(self):
        s = self.segments[0]
        new_snake = self.create_snake(s.pos())
        self.segments.insert(0, new_snake)

    def is_crash(self):

        # the snake crashes itself
        for s in self.segments:
            if s != self.head and self.head.pos() == s.pos():
                print('crashes itself')
                return True

        # the snake crashes the wall
        if (self.head.xcor() > 280 or self.head.xcor() < -280 or
                self.head.ycor() > 280 or self.head.ycor() < -280):
            print('crashes the wall')
            return True

        return False
