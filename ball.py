from turtle import Turtle
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

	def moveBall(self, screen_width, screen_height):
		oldx = self.xcor()
		oldy = self.ycor()
		newx = oldx + self.dx
		newy = oldy + self.dy
		self.goto(newx,newy)
		if self.xcor() + self.radius >= screen_width:
			self.dx = -self.dx
		if self.ycor() + self.radius >= screen_height:
			self.dy = -self.dy
		if self.xcor() - self.radius <= -screen_width:
			self.dx = -self.dx
		if self.ycor() - self.radius <= -screen_height:
			self.dy = -self.dy