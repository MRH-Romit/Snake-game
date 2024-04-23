from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}       High Score: {self.high_score}",  align="center", font=('Arial', 24, 'normal'))
        
        
    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()    