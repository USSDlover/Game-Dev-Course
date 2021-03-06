import turtle
import winsound

# Game main

wn = turtle.Screen()
wn.title('Pong by @Alireza')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()

paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# Paddle B
paddle_b = turtle.Turtle()

paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Ball
ball = turtle.Turtle()

ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.speed(0)

ball.dx = .2
ball.dy = -.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))

# Key bindings

wn.listen()

wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')

wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('border.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('border.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))
        winsound.PlaySound('score.wav', winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))
        winsound.PlaySound('score.wav', winsound.SND_ASYNC)

    # Paddle and Ball collision

    if (350 > ball.xcor() > 340) and ((paddle_b.ycor() + 50) > ball.ycor() > (paddle_b.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('paddle.wav', winsound.SND_ASYNC)

    if (-350 < ball.xcor() < -340) and ((paddle_a.ycor() + 50) > ball.ycor() > (paddle_a.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('paddle.wav', winsound.SND_ASYNC)
