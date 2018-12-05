import turtle

def tree(l):
	if (l<=10):
		turtle.left(20)
		turtle.backward(l)
	else:
		turtle.forward(l)
		turtle.right(20)
	# tree(l-10)
	# if(l<=10):
	# 	turtle.backward(l)
	# 	turtle.right(20)

	# else:
	# 	turtle.forward(l)
	# 	turtle.left(20)	
	# tree(l-10)

tree(100)					
	




turtle.mainloop()