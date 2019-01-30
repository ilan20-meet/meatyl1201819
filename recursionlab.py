import turtle
def tree(l):
	if (l==0):	
		turtle.left(10)
		turtle.backward(l)
		turtle.left(20)
		
	else:	
		turtle.forward(l)
		turtle.right(10)
		tree(l-5)


tree(50)					
	




turtle.mainloop()