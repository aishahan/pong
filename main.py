#Create Screen
from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Score

turtle = Turtle()
screen = Screen()
screen.setup(width = 800, height= 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

#create both paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

score = Score()

#make paddles listen to key strokes
screen.listen()
screen.onkey(l_paddle.up,"Up")
screen.onkey(l_paddle.down,"Down")
screen.onkey(r_paddle.up,"w")
screen.onkey(r_paddle.down,"s")


game_is_on = True


while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()
    
    #Detect collision with N and S walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #Detect collision with r_paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()


    #Detect collision with l_paddle
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()


    #Detect when right paddle misses
    if ball.xcor() > 390:
        ball.reset_ball()
        score.l_point()

    #Detect when left paddle misses
    if ball.xcor() < -390:
        ball.reset_ball()
        score.r_point()


screen.exitonclick()

