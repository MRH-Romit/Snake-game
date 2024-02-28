from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

## listen button

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

screen.exitonclick()
