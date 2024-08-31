mport turtle
import winsound

#screen
sc=turtle.Screen()
sc.setup(width=800,height=600)
sc.bgcolor("Black")
sc.title("Pong")
sc.tracer()


#trayA
a=turtle.Turtle()
a.speed(0)
a.penup()
a.setpos(-350,0)
a.shape("square")
a.color("red")
a.shapesize(stretch_wid=5,stretch_len=1) #length 100 pixel breadth 20 pixel
#shapestretch stretches width by 5 times 
#trayB
b=turtle.Turtle()
b.speed(0)
b.penup()
b.setpos(350,0)
b.shape("square")
b.color("blue")
b.shapesize(stretch_wid=5,stretch_len=1) #length 100 pixel breadth 20 pixel


#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.color("white")
ball.setpos(0,0)
ball_dx=5
ball_dy=5



score_a=0
score_b=0

#writing
p=turtle.Turtle()
p.color("white")
p.penup()
p.hideturtle()
p.setpos(0,260)
p.write("Player A : 0  Player B : 0",  align='center'  ,    font=('Arial', 20, 'normal'))

#functions

#trayA

a.move_up = False
a.move_down = False

b.move_up = False
b.move_down = False


# Functions
def a_up_start():
    a.move_up = True

def a_up_end():
    a.move_up = False

def a_down_start():
    a.move_down = True

def a_down_end():
    a.move_down = False

def b_up_start():
    b.move_up = True

def b_up_end():
    b.move_up = False

def b_down_start():
    b.move_down = True

def b_down_end():
    b.move_down = False


#keyboardkeys
sc.listen()
sc.onkeypress(a_up_start, "w")  
sc.onkeyrelease(a_up_end, "w")

sc.onkeypress(a_down_start, "s")
sc.onkeyrelease(a_down_end, "s")

sc.onkeypress(b_up_start, "Up")
sc.onkeyrelease(b_up_end, "Up")

sc.onkeypress(b_down_start, "Down")
sc.onkeyrelease(b_down_end, "Down")



while(True):
  sc.update()

  #Smooth_Movement_OF_A
  if a.move_up:
    if a.ycor() < 250:
      y = a.ycor()
      y += 20
      a.sety(y)

  if a.move_down:
    if a.ycor() > -250:
      y = a.ycor()
      y -= 20
      a.sety(y)
  #Smooth_Movement_OF_B
  if b.move_up:
    if b.ycor() < 250:
      y = b.ycor()
      y += 20
      b.sety(y)

  if b.move_down:
    if b.ycor() > -250:
      y = b.ycor()
      y -= 20
      b.sety(y)

  #move the ball
  ball.setx(ball.xcor() + ball_dx)
  ball.sety(ball.ycor() + ball_dy)

  #ball rebound with top and bottom
  if ball.ycor()>290 :
    ball.sety(290)
    ball_dy*=-1
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

  elif ball.ycor()<-290 :
    ball.sety(-290)
    ball_dy*=-1
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
  
  
  #ball right and left
  if ball.xcor() > 360:
        score_a += 1
        p.clear()
        p.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=('Arial', 20, 'normal'))
        ball.goto(0, 0)
        ball_dx=6
        ball_dy=6
        ball_dx *= -1

  elif ball.xcor() < -360:
        score_b += 1
        p.clear()
        p.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=('Arial', 20, 'normal'))
        ball.goto(0, 0)
        ball_dx=6
        ball_dy=6
        ball_dx *= -1
  
#ball and trayA collide
  if ball.xcor() < -340 and ball.ycor() < a.ycor() + 70 and ball.ycor() > a.ycor() - 70:  
        if (ball.ycor())-10<(a.ycor()):
          ball_dy*=-1.03
        ball_dx *= -1.03 #com of trayA lies at x coord of-350 since width is 20 pixel i.e 10+10 thats why condition is less than -340
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
  #ball and trayB collide
  elif ball.xcor() > 340 and ball.ycor() < b.ycor() + 70 and ball.ycor() > b.ycor() - 70:
    if (ball.ycor())-10<(b.ycor()):
          ball_dy*=-1.03
    ball_dx *= -1.03
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
