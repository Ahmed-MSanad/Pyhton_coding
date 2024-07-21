from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game.")
screen.tracer(0) # turn off the tracer


snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun=snake.to_top, key="Up")
screen.onkey(fun=snake.to_down, key="Down")
screen.onkey(fun=snake.to_right, key="Right")
screen.onkey(fun=snake.to_left, key="Left")

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food:
    if snake.head.distance(food) < 15:
        snake.increase_snake_length()
        scoreboard.increase_score()
        food.set_food()
    
    # Detect collision with wall:
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with tail:
    for segment in snake.snakeParts[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
