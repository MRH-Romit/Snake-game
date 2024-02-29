from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))
        self.clear()