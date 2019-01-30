import turtle
def tree(l):
	if (l>5):	
		turtle.forward(l)
		turtle.right(10)
		tree(l-5)
		turtle.left(10)
		turtle.backward(l)
		turtle.left(20)
		tree(l-5)
		turtle.right(20)
		turtle.forward(l)
		

tree(50)					
	




turtle.mainloop()