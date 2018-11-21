import turtle
from turtle import Turtle
import random
turtle.colormode(255)
# class Square(Turtle):
# 	def __init__(self,size):
# 		Turtle.__init__(self)
# 		self.shape("square")
# 		self.shapesize(size)
# 	def random_color(self):
		
# 		self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		self.setheading(90)	
		turtle.register_shape("rectangle",((0,0),(width,0),(width,height),(0,height)))
		self.shape("rectangle")

class Square(Rectangle):
	def __init__(self, side):
		Rectangle.__init__(self,side,side)

class Hexagon(Turtle):
	def __init__(self, length):
		Turtle.__init__(self)
		self.length = length
		self.setheading(0)
		turtle.register_shape("hexa",((0,0),(self.length,0),(0.5*self.length+self.length,0.8660254*self.length),(self.length,2*0.8660254*self.length),(0,2*0.8660254*self.length),((-0.5)*self.length,0.8660254*self.length),(0,0)))
		self.shape("hexa")
#sqr = Square(100)
#Hex = Hexagon(100)

class Polygon(Turtle):
	def __init__(self,lines,length):
		Turtle.__init__(self)
		self.lines = lines
		self.length = length
		turtle.hideturtle()
		turtle.penup()
		turtle.begin_poly()
		for i in range(lines):
			turtle.forward(length)
			turtle.left(360/lines)
		turtle.end_poly()	
		polygon = turtle.get_poly()
		turtle.register_shape("polygon", polygon)
		self.shape("polygon")
		self.setheading(45)
	def moveShape(self, speed):
		self.speed = speed
		self.goto	
test = Polygon(8,60)
# while True:
# 	while test.pos()[0] < 300 or test.pos()[0] > -300 or test.post()[1] < 300 or test.post()[1] > -300:
# 		test.forward(1)
# 	test.left(90)	
turtle.mainloop()		
