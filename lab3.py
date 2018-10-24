import turtle

turtle.register_shape("bottle.gif")
turtle.shape("bottle.gif")
turtle.speed(10000000000000)
for i in range(362):
	
	turtle.forward(300)
	turtle.right(45)
	turtle.forward(150)
	turtle.right(90)
	turtle.forward(25)
	turtle.pensize(2)
	turtle.forward(25)
	turtle.pensize(1)
	turtle.forward(25)
	turtle.home()
	turtle.right(i)
turtle.mainloop()





