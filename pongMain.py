# Main code for pong game
# Import modules
import _tkinter
from turtle import Turtle, Screen
from pongPaddle import Paddle
from pongBall import Ball
from pongScoreboard import Scoreboard
import time

# Set variable for game being on
game_is_on = True
# Set up screen to be 800x600 and black
screen = Screen()
screen.setup(width = 800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# Pause the animation whil game is being set up
screen.tracer(0)

# Create the left paddle. Position it at left of screen
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# Create ball
ball = Ball()

# Create scoreboard objects
scoreboard = Scoreboard()

# Call listen method so we can start controlling paddles with keys
screen.listen()

# Keys will control movement of left paddle
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

# Keys will control movement of right paddle
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

# While the game is on
while game_is_on:
    # Update screen but delay by the move speed of the ball
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce off wall so call bounce method
        ball.bounce_y()
    
    # Detect collision with paddle
    # If the distance from a paddle is less than 50
    # AND the ball is within 60 pixels from side of screen,
    # we can assume it has collided with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 390:
        ball.refresh()
        # Left gets point
        scoreboard.l_point()

    # Detect if left paddle misses
    if ball.xcor() < -390:
        ball.refresh()
        # Right gets point
        scoreboard.r_point()

    # When a player wins by scoring 10 points
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.game_over()
        game_is_on = False

# Only exit the screen when clicked
screen.exitonclick()