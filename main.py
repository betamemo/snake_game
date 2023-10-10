import time
from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard
from snake import Snake

# background
screen = Screen()
screen.screensize(300, 300, 'lightyellow')
screen.addshape('img/apple.gif')
screen.listen()

# scoreboard
scoreboard = Scoreboard()
scoreboard.print_score()

turtle = Turtle()
snake = Snake()
food = Food()

# controller
screen.onkeypress(fun=snake.go_up, key='Up')
screen.onkeypress(fun=snake.go_down, key='Down')
screen.onkeypress(fun=snake.go_left, key='Left')
screen.onkeypress(fun=snake.go_right, key='Right')

is_on = True
while is_on:
    time.sleep(0.1)  # snake's speed
    snake.move()
    if snake.head.distance(food) < 20:
        print('nom nom nom')
        scoreboard.add_score(10)  # increase score
        snake.extend_snake()  # extend snake
        food.food_pos()  # move food

    # the snake crashes the wall or itself
    if snake.is_crash():
        print('game over')
        scoreboard.game_over()
        is_on = False

screen.mainloop()
