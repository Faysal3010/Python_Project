from turtle import Turtle

CENTER = "center"
FONT = ('courier', 12, 'normal')
GAME_OVER="Game Over"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align=CENTER, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(GAME_OVER, align=CENTER, font=('courier', 30, 'normal'))
        
