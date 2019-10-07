import turtle
import os
import math
import random

#screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.bgpic("background.gif")

#register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

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

#set and draw the score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_str = "Score: %s"%score
score_pen.write(score_str, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#player setup
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
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
bullet_speed = 40
bullet_state = "ready"

def fire_bullet():
	global bullet_state
	if bullet_state == "ready":
		os.system("afplay shoot.wav&")
		bullet_state = "fire" 
		bullet.setposition(player.xcor(), player.ycor() + 10)
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

#collision 
def is_collision(t1, t2):
	x_sq = math.pow(t1.xcor() - t2.xcor(), 2)
	y_sq = math.pow(t1.ycor() - t2.ycor(), 2)
	distance = math.sqrt(x_sq + y_sq)
	if distance <= 20:
		return True
	else:
		return False

#enemy
num_enemy = 5
enemies = []
for _ in range(0, num_enemy):
	enemies.append(turtle.Turtle())
for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)
enemy_speed = 2

#keyboard binding
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#main game loop
while True:
	#move enemies
	for enemy in enemies:
		enemyx = enemy.xcor() + enemy_speed
		enemy.setx(enemyx)
		#enemy reverse direction and down
		if enemy.xcor() > 280 or enemy.xcor() < -280:
			for e in enemies:
				e.sety(e.ycor() - 40) 
			enemy_speed *= -1
		#check for collision between the enemy and bullet
		if is_collision(bullet, enemy):
			os.system("afplay explosion.wav&")
			bullet.hideturtle()
			bullet.setposition(0, -300)
			bullet_state = "ready"
			os.system("afplay reload.wav&")
			enemy.setposition(random.randint(-200, 200), random.randint(100, 250))
			enemyx = enemy.xcor() + enemy_speed
			enemy.setx(enemyx)
			score += 10
			score_str = "Score: %s"%score
			score_pen.clear()
			score_pen.write(score_str, False, align="left", font=("Arial", 14, "normal"))

		if is_collision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print("Game Over")
			break
	
	#move bullet
	if bullet_state == "fire":
		bullet.sety(bullet.ycor() + bullet_speed)

	#bullet check
	if bullet.ycor() > 280:
		bullet.hideturtle()
		if bullet_state != "ready":
			os.system("afplay reload.wav&")
		bullet_state = "ready"

	 
	 
delay = input("Press enter to finish")