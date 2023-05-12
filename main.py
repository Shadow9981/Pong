from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.tracer(0)
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)

game_running = True

while game_running:
    screen.update()
    ball.move_ball()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
        ball.increase_speed()
        print(ball.x_move)

    if ball.xcor() > 400:
        scoreboard.r_score_increase()
        ball.goto(0, 0)
        ball.reset_speed()
        ball.bounce_x()

    if ball.xcor() < -400:
        scoreboard.l_score_increase()
        ball.goto(0, 0)
        ball.reset_speed()
        ball.bounce_x()

screen.exitonclick()
