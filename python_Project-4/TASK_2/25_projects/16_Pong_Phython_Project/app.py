import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create paddles and ball
paddle_a = turtle.Turtle()
paddle_b = turtle.Turtle()
ball = turtle.Turtle()

# Paddle A
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # Ball's x-axis movement speed
ball.dy = 2  # Ball's y-axis movement speed

# Score variables
score_a = 0
score_b = 0

# Pen (for displaying scores)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y < 250:  # Prevent paddle from going out of bounds
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y > -250:
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y < 250:
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y > -250:
        paddle_b.sety(y)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (top and bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Border checking (left and right)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1