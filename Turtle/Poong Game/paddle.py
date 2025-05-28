from turtle import Turtle,Screen

s=Screen()
s.listen()

class Paddle(Turtle):
     
    
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4,1)
        self.penup()
        self.goto(position,0)

    def go_up(self):
        new_y=self.ycor()+15
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y=self.ycor()-15
        self.goto(self.xcor(),new_y)

    def right_move(self):
        s.onkey(self.go_up,"Up")
        s.onkey(self.go_down,"Down")

    def left_move(self):
        s.onkey(self.go_up,"w")
        s.onkey(self.go_down,"s")




        
                