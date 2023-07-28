# Paddles for the pong game
# Import modules
import _tkinter
from turtle import Turtle

# Constants for directions to be used in move method
UP = 90
DOWN = 270

# Class for paddle inherits from Turtle class
class Paddle(Turtle):
    # Takes x and y positions for where it should start
    def __init__(self, x_pos, y_pos):
        # Make sure the Class is initialised
        super().__init__()
        # Lift pen up so it doesn't draw a line
        self.penup()
        # Set colour to white
        self.color("white")
        # Make it a square shape
        self.shape("square")
        # Stretch the shape so it has a width of 20 and height of 100
        self.shapesize(stretch_len=1, stretch_wid=5)
        # Move it too its starting position
        self.setpos(x_pos, y_pos)
    
    # Method for moving up
    def move_up(self):
        # Move it up by 20 pixels but only if is within screen
        if self.ycor() <= 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
    
    # Method for moving down
    def move_down(self):
        # Move it down by 20 pixels but only if is within screen
        if self.ycor() >= -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)