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
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


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
 
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        ScoreBoard.game_over()
    
## detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            ScoreBoard.game_over()


screen.exitonclick()
