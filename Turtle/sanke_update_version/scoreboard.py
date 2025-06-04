from turtle import Turtle


CENTER = "center"
FONT = ('courier', 12, 'normal')
GAME_OVER = "Game Over"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("sanke_update_version/data.txt", mode='r') as data:
            self.high_score = int(data.read())
        with open("sanke_update_version/name.txt", mode='r') as name_file:
            self.name = name_file.read()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score = {self.score}; {self.name}High_Score = {self.high_score}", align=CENTER, font=FONT)

    def increse_score(self):
        self.score += 1
        self.update_score()

    def highest_score(self, name):
        self.high_score = self.score
        with open("sanke_update_version/data.txt", mode='w') as file:
            file.write(str(self.high_score))
        with open("sanke_update_version/name.txt", mode='w') as file:
            file.write(name.upper()+'->')
        self.goto(0, 0)
        self.write(f"\tCongratulation {name.upper()}!\nYou have done the highest score:{self.high_score}", align=CENTER, font=(
            'courier', 15, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(GAME_OVER, align=CENTER, font=('courier', 30, 'bold'))
