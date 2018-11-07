import turtle

def tree(l):
	if (l<=10):
		turtle.backwards(l)
		turtle.left(20)
	else:
		turtle.forward(l)
		turtle.right(20)
	tree(l-10)
	if(l<=10):
		turtle.backwards(l)
		turtle.right(20)

	else:
		turtle.forward(l)
		turtle.left(20)	
	tree(l-10)

tree(100)					
	




turtle.mainloop()