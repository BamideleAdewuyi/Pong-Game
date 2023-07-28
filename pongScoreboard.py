# Scoreboard for pong game
# Import modules
import _tkinter
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        # Attributes for scores of each player
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    # Method for updating scores
    def update_scoreboard(self):
        # Clear scoreboard first
        self.clear()
        # Left player score position and formatting
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # Right player score position and formatting
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    
    # Method for awarding left player a point
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Method for awarding right player a point
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    
    # Method for game being over
    def game_over(self):
        self.goto(0, 0)
        if self.r_score > self.l_score:
            self.write("Game over, right player wins!", align="center", font=("Courier", 40, "normal"))
        else:
            self.write("Game over, left player wins!", align="center", font=("Courier", 40, "normal"))