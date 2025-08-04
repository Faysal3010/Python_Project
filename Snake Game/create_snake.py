from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segment = []
        self.create()
        self.head=self.segment[0]
        self.box()


    def box(self):
        line=Turtle()
        line.color("white")
        line.hideturtle()
        line.width(2)
        line.penup()
        line.goto(-470,270)
        line.pendown()
        line.goto(470,270)
        line.goto(470,-270)
        line.goto(-470,-270)
        line.goto(-470,270)


    def create(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    
    def add_segment(self,position):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.segment.append(t)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        n=len(self.segment)
        for i in range(n-1,0,-1):
            x=self.segment[i-1].xcor()
            y=self.segment[i-1].ycor()
            self.segment[i].goto(x,y)
        self.head.fd(MOVING)


    def reset(self):
        for seg in self.segment:
            seg.hideturtle()
        self.segment.clear()
        self.create()
        self.head=self.segment[0]

    def up(self): 
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)               
    def down(self): 
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)               
    def right(self): 
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)               
    def left(self): 
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)               
                   
