import turtle

# Screen setup
wn = turtle.Screen()
wn.title('Pong by Imrie83')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.025
ball.dy = 0.025

# Turtle Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A {score_a} - {score_b} Player B", align="center", font=("Courier", 16, "bold"))



# Paddle movement Functions
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)


def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)


def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)


def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_left_up, "w")
wn.onkeypress(paddle_left_down, "s")
wn.onkeypress(paddle_right_up, "Up")
wn.onkeypress(paddle_right_down, "Down")

# Main loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checks
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A {score_a} - {score_b} Player B", align="center", font=("Courier", 16, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A {score_a} - {score_b} Player B", align="center", font=("Courier", 16, "bold"))

    # Paddle / Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 50
                                                      and ball.ycor() > paddle_right.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 50
                                                        and ball.ycor() > paddle_left.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
