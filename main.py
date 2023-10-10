from turtle import Screen, Turtle

from food import Food
from snake import Snake

screen = Screen()
screen.bgcolor('black')
screen.addshape('img/apple.gif')
screen.listen()

turtle = Turtle()
snake = Snake()
food = Food()

screen.onkeypress(fun=snake.go_up, key='Up')
screen.onkeypress(fun=snake.go_down, key='Down')
screen.onkeypress(fun=snake.go_left, key='Left')
screen.onkeypress(fun=snake.go_right, key='Right')

screen.mainloop()
