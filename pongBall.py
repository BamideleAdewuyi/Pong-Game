# Ball for pong game
# Import modules
import _tkinter
from turtle import Turtle


# Create class for ball that inherits from Turtle class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # Attributes that determine which direction on the x and y
        # axes the ball travels
        self.x_move = 10
        self.y_move = 10
        # Set a movement speed attribute so that we can increase the speed
        # when it gets hit
        self.move_speed = 0.1

    # Method for moving
    def move(self):
        # Moves in direction as defined by its attributes. This makes
        # bouncing possible
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)
    
    # Method for bouncing off walls (y axis)
    def bounce_y(self):
        # Change the way it is moving in y axis by multiplying by -1
        self.y_move *= -1

    # Method for bouncing off paddle (x axis)
    def bounce_x(self):
        # Change the way it is moving in x axis by multiplying by -1
        self.x_move *= -1
        # Set new move speed every time it gets hit by paddle
        self.move_speed *= 0.9
    
    # Method for refreshing ball if it goes out of play
    def refresh(self):
        # Return to centre
        self.goto(0, 0)
        # Go in opposite direction
        self.x_move *= -1
        # Reset move speed
        self.move_speed = 0.1