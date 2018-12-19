import turtle
from turtle import Turtle
import random 
turtle.tracer(0)
class Ball(Turtle):
	def __init__(self, radius, color, x, y, dx,dy):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
	def moveBall(self):
		oldx = self.xcor()
		oldy = self.ycor()
		newx = oldx + self.dx
		newy = oldy + self.dy
		self.goto(newx,newy)
		if self.xcor() + self.radius >= 450:
			self.dx = -self.dx
		if self.ycor() + self.radius >= 400:
			self.dy = -self.dy
		if self.xcor() - self.radius <= -450:
			self.dx = -self.dx
		if self.ycor() - self.radius <= -400:
			self.dy = -self.dy
def collision(ball1,ball2,choice):
	radius_sum = ball1.radius + ball2.radius
	d = ((ball1.xcor() - ball2.xcor())**2 + (ball1.ycor() - ball2.ycor())**2)**0.5
	if(d < radius_sum):
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
				ball1.goto(random.randint(-450+ball1.radius,450-ball1.radius),random.randint(-400+ball1.radius,400-ball1.radius))
				ball2.radius+=2
				ball2.shapesize(ball2.radius/10)
			else:
				ball2.goto(random.randint(-450+ball2.radius,450-ball2.radius),random.randint(-400+ball2.radius,400-ball2.radius))
				ball1.radius+=2
				ball1.shapesize(ball1.radius/10)
def func(event):
    ball3.goto(event.x-475, 405-event.y)
border = Turtle()
border.hideturtle()
border.penup()
border.goto(450,400)
border.pendown()
border.goto(450,-400)
border.goto(-450,-400)
border.goto(-450,400)
border.goto(450,400)
ball1 = Ball(60,"blue", 200, 200, .4, .4)		
ball2 = Ball(45,"orange", 0, 0, .10, .10)
ball3 = Ball(50,"cyan",-200,-200,0,0)	
wn = turtle.Screen()
screen = wn.getcanvas()
screen.bind('<Motion>', func)
while True:
	ball1.moveBall()
	ball2.moveBall()
	collision(ball1,ball2,'eat')
	turtle.update()
		
turtle.mainloop()