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
		self.setheading(90)
		Turtle.register_shape("hexa",((0,0),(self.length,0),(0.5*self.length+self.length,self.length),(self.length,2*self.length),(0,2*self.length),((-0.5)*self.length,self.length),(0,0)))
		self.shape("hexa")
#sqr = Square(100)
Hex = Hexagon(30)
turtle.mainloop()		
