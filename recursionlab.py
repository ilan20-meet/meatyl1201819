import turtle
def tree(l):
	if (l>0):
		turtle.forward(l)
		return tree(l-10)
	else:
		turtle.left(5)
		turtle.forward(l)
		return tree(l-10)

					
	
tree(200)




turtle.mainloop()