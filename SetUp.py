import turtle
import os

#screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

#border setup
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(2)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#player setup
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 15

#weapon setup
bullet = turtle.Turtle()
bullet.color("orange")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bullet_speed = 20
bulletstate = "ready"

def fire_bullet():
	global bulletstate
	x = player.xcor()
	y = player.ycor() + 10
	#bullet.setpostion(x, y)
	bullet.showturtle()

#move left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

#enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemy_speed = 2

#keyboard binding
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#main game loop
while True:
	enemyx = enemy.xcor()
	enemy.setx(enemyx + enemy_speed)
	
	#move bullet
	bullet.sety(bullet.ycor() + bullet_speed)
	
	#enemy reverse direction
	if enemy.xcor() > 280 or enemy.xcor() < -280:
		enemy.sety(enemy.ycor() - 40)
		enemy_speed *= -1
	 
delay = input("Press enter to finish")