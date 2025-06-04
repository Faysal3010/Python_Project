from turtle import Screen
from create_snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


s = Screen()
s.bgcolor("black")
s.setup(1000, 600)
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


def decision():
    
    if scoreboard.score>scoreboard.high_score:
        user_input=s.textinput(title="", prompt="Enter your name: ")
        scoreboard.highest_score(user_input)
    else:
        scoreboard.game_over()


is_on = True
while is_on:
    s.update()
    time.sleep(0.08)
    snake.move()

    # detect collisition to food
    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()

    # detect collisition to wall

    if not -470 < snake.head.xcor() < 470 or not -270 < snake.head.ycor() < 270:
        is_on = False
        decision()
        # snake.reset()
    
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            is_on = False
            decision()


s.exitonclick()
