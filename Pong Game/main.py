from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score_board import Scoreboard

s = Screen()
s.tracer(0)
s.bgcolor("black")
s.setup(800, 600)
s.title("Pong Game")

ball = Ball()
left_scoreboard=Scoreboard(-150)
right_scoreboard=Scoreboard(150)

right_paddle = Paddle((350))
left_paddle = Paddle((-350))

right_paddle.right_move()
left_paddle.left_move()

is_game_on = True
while is_game_on:
    s.update()
    sleep(ball.move_speed)
    ball.move()

    # ball is collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        """needs to bounce"""
        ball.bounce_wall()
    # ball is collision with the left and right padding
    if (ball.distance(right_paddle) < 40 and ball.xcor() > 330) or (ball.distance(left_paddle) < 40 and ball.xcor() < -330):
        ball.bounce_paddle()

    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor()>400:
            left_scoreboard.increase_left()
        elif ball.xcor()<-400:
            right_scoreboard.increase_right()

        ball.reset_position()


s.exitonclick()
