from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("#fff")
        self.penup()
        self.setposition(0, 250)
        self.hideturtle()
        self.set_score()
    
    def set_score(self):
        self.write(f"Current score is: {self.score}", False, ALIGNMENT,FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.set_score()
    
    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align=ALIGNMENT, font=FONT)
