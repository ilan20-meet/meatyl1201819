from turtle import *
import random 

class Ball(Turtle):
	def __init__(self, radius, color, x, y, dx,dy):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.goto(x,y)
		
	def moveBall(self):
		oldx = self.xcor()
		oldy = self.ycor()
		newx = oldx + dx
		newy = oldy + dy
def collision(ball1,ball2):
	radius_sum = ball1.radius + ball2.radius
	d = ((ball1.xcor() - ball2.xcor())**2 + (ball1.ycor() - ball2.ycor())**2)**0.5
	if(d < radius_sum):
		return True
	else:
		return False	

ball1 = Ball(50,"blue", 0, 0, 1, 1)		
ball2 = Ball(50,"orange", 0, 0, 1, 1)	

mainloop()