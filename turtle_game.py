import turtle
import math
import random
import os
import time

# Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("kbgame-bg.gif")
wn.tracer(7)

# Draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

# Create obstacles
maxObsts = 20
obsts = []

for count in range(maxObsts):
    obsts.append(turtle.Turtle())
    obsts[count].color("yellow")
    obsts[count].shape("square")
    obsts[count].penup()
    obsts[count].speed(0)
    obsts[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

# Create the score variable
score = 0

# Create goals
maxGoals = 10
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-280, 280), random.randint(-280, 280))

# Set speed variablemypen.undo()
speed = 1


# Define function
def turnleft():
    player.left(30)


def turnright():
    player.right(30)


def increasespeed():
    global speed
    speed += 1


def decresespeed():
    global speed
    if speed > 0:
        speed -= 1
    elif speed == 0:
        pass
    else:
        speed = 0


def isCollision(t1, t2):
    d = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    if d < 20:
        return True
    else:
        return False


# Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decresespeed, "Down")

start = time.time()

while True:
    player.forward(speed)
    now = time.time()
    # print(now - start)
    # Draw the elapsed time on th screen
    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(0, 310)
    mypen.write(now - start, False, align="left", font=("Ubuntu", 14, "normal"))

    # Draw the score on the screen
    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(-290, 310)
    scorestirng = "Score: %s" % score
    mypen.write(scorestirng, False, align="left", font=("Ubuntu", 14, "normal"))

    # Boundary Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        os.system("mplayer bounce.mp3&")

    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        os.system("mplayer bounce.mp3&")

    # Move the goals
    for count in range(maxGoals):
        goals[count].forward(3)

        # Boundary Checking
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
            os.system("mplayer bounce.mp3&")

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
            os.system("mplayer bounce.mp3&")

        # Collision checking for player and goals
        if isCollision(player, goals[count]):
            goals[count].setposition(
                random.randint(-280, 280), random.randint(-280, 280)
            )
            goals[count].right(random.randint(0, 360))
            os.system("mplayer collision.mp3&")
            score += 1

    for count in range(maxObsts):
        # Collision checking for player and obstacles
        if isCollision(player, obsts[count]):
            # os.system("mplayer collision.mp3&")
            score -= 1


delay = input("Press Enter to finish.")
