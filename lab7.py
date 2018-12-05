from turtle import *
import random 
tracer(0)
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
		if self.xcor() + self.radius >= 600:
			self.dx = -self.dx
		if self.ycor() + self.radius >= 400:
			self.dy = -self.dy
		if self.xcor() - self.radius <= -600:
			self.dx = -self.dx
		if self.ycor() - self.radius <= -400:
			self.dy = -self.dy
def collision(ball1,ball2):
	radius_sum = ball1.radius + ball2.radius
	d = ((ball1.xcor() - ball2.xcor())**2 + (ball1.ycor() - ball2.ycor())**2)**0.5
	if(d < radius_sum):
		tempX =  ball1.dx
		tempY = ball1.dy
		ball1.dx = ball2.dx
		ball1.dy = ball2.dy
		ball2.dx = tempX
		ball2.dy = tempY
			

ball1 = Ball(50,"blue", 200, 200, .4, .4)		
ball2 = Ball(50,"orange", 0, 0, .10, .10)	
while True:
	ball1.moveBall()
	ball2.moveBall()
	collision(ball1,ball2)
	update()
		
mainloop()