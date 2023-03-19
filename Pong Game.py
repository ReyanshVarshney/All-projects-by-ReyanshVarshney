import turtle
import winsound
wn=turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Scoring
score_1 = 0
score_2 = 0



#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(+350, 0)


#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.025

#Pen
pen = turtle.Turtle()
pen.speed(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center" , font=("Calibri", 24, "normal"))

#Function
def paddle_a_up():
    y= paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y= paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y= paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y= paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Game Loop
while True:
    wn.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
       

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
       

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1+=1
        pen.write("Player 1:{}   Player 2: {}".format(score_1, score_2), align="center" , font=("Calibri", 24, "normal"))
        pen.clear()
        pen.write("Player 1:{}   Player 2: {}".format(score_1, score_2), align="center" , font=("Calibri", 24, "normal"))
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
       
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2+=1
        pen.write("Player 1:{}   Player 2: {}".format(score_1, score_2), align="center" , font=("Calibri", 24, "normal"))
        pen.clear()
        pen.write("Player 1:{}   Player 2: {}".format(score_1, score_2), align="center" , font=("Calibri", 24, "normal"))
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
    