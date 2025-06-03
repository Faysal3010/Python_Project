import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.onkey(player.go_up, "Up")
# screen.onkey(player.go_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.finish_line_y() == True:
        car_manager.speed_up()
        scoreboard.increase()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

scoreboard.game_over()
screen.exitonclick()
