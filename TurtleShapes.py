import turtle

#colours = ["blue","green","red","purple","pink"]
#for i in range(5):
#	turtle.color(colours[i])
#	turtle.forward(100)
#	turtle.right(144)
turtle.begin_poly()
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(55)
turtle.right(40)
turtle.forward(40)
turtle.right(100)
turtle.forward(40)
turtle.right(40)
turtle.forward(55)

turtle.end_fill()
turtle.end_poly()
s=turtle.get_poly()
turtle.register_shape("niceshape",s)
turtle.mainloop()
