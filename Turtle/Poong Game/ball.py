from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed=0.01

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1
        print(f"Collision to wall : {self.pos()}")

    def bounce_paddle(self):
        self.x_move *= -1
        # if self.move_speed>0.005:
        #     self.move_speed-=0.005
        '''or'''
        self.move_speed*=0.9
        print(f"Collision to paddle : {self.pos()}")
        print(f"Ball Speed: {round(self.move_speed,4)}")

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed=0.01
        self.x_move *= -1
        self.y_move *= -1
             