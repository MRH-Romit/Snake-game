from turtle import Screen
import time
from snake import Snake
from food import Food
from ScoreBoard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
ScoreBoard = ScoreBoard()
food = Food()

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
    
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        ScoreBoard.increase_score()
        ScoreBoard.update_scoreboard()
        
## detect collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        ScoreBoard.game_over()
    

screen.exitonclick()
