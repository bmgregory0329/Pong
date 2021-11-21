import turtle
import winsound
import time

# Window Config -----------------------------------

wn = turtle.Screen() # creating the window
wn.title("Pong by Brian Gregory") # window title
wn.bgcolor("black") # background color
wn.setup(width=800, height=600) # window size
wn.tracer(0) # speed up games by manually updating

# Score Config ------------------------------------

score_a = 0
score_b = 0

# Paddle A Config ---------------------------------

paddle_a = turtle.Turtle() # call upon the turtle class/module for config
paddle_a.speed(0) # max speed
paddle_a.shape("square") # built in shape
paddle_a.color("white") # paddle color
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # 20x20 pixles default, mult by 5x1
paddle_a.penup() # draws line by default as moving so don't do that
paddle_a.goto(-350,0)

# Paddle B Config ---------------------------------

paddle_b = turtle.Turtle() # call upon the turtle class/module for config
paddle_b.speed(0) # max speed
paddle_b.shape("square") # built in shape
paddle_b.color("white") # paddle color
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # 20x20 pixles default, mult by 5x1
paddle_b.penup() # draws line by default as moving so don't do that
paddle_b.goto(350,0)

# Ball Config -------------------------------------

ball = turtle.Turtle() # call upon the turtle class/module for config
ball.speed(0) # max speed
ball.shape("square") # built in shape
ball.color("white") # paddle color
ball.penup() # draws line by default as moving so don't do that
ball.goto(0,0) # put ball in middle
ball.dx = .1 # ball movement speed in pixels
ball.dy = .1 # ball movement speed in pixels

# Pen ---------------------------------------------

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,-280)
pen2.write("Move Up: W or Up Arrow      Move Down: S or Down Arrow", align="center", font=("Courier",10,"normal"))

# Movement Function -------------------------------

def paddle_a_up():
    y = paddle_a.ycor() # grab current y-coordinate
    y += 20 # add 20 pixles to y-coordinate
    paddle_a.sety(y) # set paddle_a

def paddle_a_down():
    y = paddle_a.ycor() # grab current y-coordinate
    y -= 20 # add 20 pixles to y-coordinate
    paddle_a.sety(y) # set paddle_a = y

def paddle_b_up():
    y = paddle_b.ycor() # grab current y-coordinate
    y += 20 # add 20 pixles to y-coordinate
    paddle_b.sety(y) # set paddle_b

def paddle_b_down():
    y = paddle_b.ycor() # grab current y-coordinate
    y -= 20 # add 20 pixles to y-coordinate
    paddle_b.sety(y) # set paddle_b = y

# Keyboard Binding --------------------------------

wn.listen() # listen for keyboard
wn.onkeypress(paddle_a_up, "w") # setting w as paddle_a up
wn.onkeypress(paddle_a_down, "s") # setting s as paddle_a_down
wn.onkeypress(paddle_b_up, "Up") # setting up arrow as paddle_b up
wn.onkeypress(paddle_b_down, "Down") # setting down arrow as paddle_b_down

# Main Game Loop ----------------------------------

wn.update()
time.sleep(2)

while True:
    wn.update()

    
        
    # Move the ball -------------------------------

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking -----------------------------

    if ball.ycor() > 290: # Window size / 2 - 20 pixels
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC) # import sound effect
        
    if ball.ycor() < -283: # Window size / 2 - 20 pixels
        ball.sety(-283)
        ball.dy *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier",24,"normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier",24,"normal"))
    
    # Paddle Ball Collision -----------------------

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)






        
