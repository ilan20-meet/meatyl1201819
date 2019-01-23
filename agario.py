
import turtle
import time
import random
from ball import Ball
import sched, time

turtle.tracer(0)
turtle.listen()
turtle.hideturtle()
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
RUNNING = True
SLEEP = 0.0077

DEATH_COUNT = 0

s = time.time()

#a function that makes the larger ball grow and the smaller ball teleport if they collide


def func(event):
    MY_BALL.goto(event.x-475, 405-event.y)

def collision(ball1,ball2,choice):
	radius_sum = ball1.radius + ball2.radius
	d = ((ball1.xcor() - ball2.xcor())**2 + (ball1.ycor() - ball2.ycor())**2)**0.5
	if(d < radius_sum and time.time() >= s + 3):
		# --SWAP DIRECTIONS--
		if choice == 'swapDirections':
			tempX =  ball1.dx
			tempY = ball1.dy
			ball1.dx = ball2.dx
			ball1.dy = ball2.dy
			ball2.dx = tempX
			ball2.dy = tempY
		elif choice == 'eat':
			if ball1.radius < ball2.radius:
				ball1.goto(random.randint(-SCREEN_WIDTH+ball1.radius,SCREEN_WIDTH-ball1.radius),random.randint(-SCREEN_HEIGHT+ball1.radius,SCREEN_HEIGHT-ball1.radius))
				ball1.radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				ball1.shapesize(ball1.radius/10)
				ball2.radius+=2
				ball2.shapesize(ball2.radius/10)
				return False	
			else:
				ball2.goto(random.randint(-SCREEN_WIDTH+ball2.radius,SCREEN_WIDTH-ball2.radius),random.randint(-SCREEN_HEIGHT+ball2.radius,SCREEN_HEIGHT-ball2.radius))
				ball2.radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				ball2.shapesize(ball2.radius/10)
				ball1.radius+=2
				ball1.shapesize(ball1.radius/10)
				return True	
			
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 50
MAXIMUM_BALL_RADIUS = 80
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

MY_BALL = Ball(65,"cyan",-200,-200,0,0)				

wn = turtle.Screen()
screen = wn.getcanvas()
screen.bind('<Motion>', func)

for i in range(NUMBER_OF_BALLS):
	radius = 0
	colour1 = random.random()
	colour2 = random.random()
	colour3 = random.random()
	dx = 0
	dy = 0
	while (dx == 0 or dy == 0 or radius == 0):
		radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
		dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

	BALLS.append(Ball(random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS),
		(colour1,colour2,colour3),
		random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS),
		random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS) , dx, dy))

while RUNNING:
	print(DEATH_COUNT)
	win = False
	for i in range(NUMBER_OF_BALLS):
		BALLS[i].moveBall(SCREEN_WIDTH,SCREEN_HEIGHT)
		for j in range(NUMBER_OF_BALLS):
			if i!=j:
				collision(BALLS[i],BALLS[j],'eat')
		if(collision(BALLS[i],MY_BALL,'eat')):
			DEATH_COUNT+=1		
		elif(MY_BALL.radius >= 330):
			win = True	
	turtle.update()
	time.sleep(SLEEP)
	if(DEATH_COUNT > 3):
		break
	if(win):
		break	
turtle.mainloop()