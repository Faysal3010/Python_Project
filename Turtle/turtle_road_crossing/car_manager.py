from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):

        x = random.randint(1, 6)
        if x == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.goto(300, random.randint(-230, 250))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)
            print(len(self.all_cars))

    def move(self):
        for x in self.all_cars:
            x.backward(self.speed)
            if x.xcor() < -320:
                self.all_cars.remove(x)
                x.hideturtle()
                

    # def remove_car(self):
    #     for x in self.all_cars:
            

    def speed_up(self):
        self.speed += MOVE_INCREMENT
