import random
# def first_last(list1):
# 	list2 = []
# 	list2.append(list1[0])
# 	list2.append(list1[-1])
# 	return(list2)
# print(first_last([1,2,3,4]))

# def under5(list1):
# 	list2=[]
# 	y=int(input("enter a number"))
# 	for x in list1:
# 		if x < y:
# 			list2.append(x)
# 	return(list2)		
# print(under5([1,2,3,4,5,6,7,8,9,10]))

def common(list1,list2):
	list3=[]
	for x in list1:
		for y in list2:
			if x==y:
				list3.append(x)
	return list3			
print(common([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

list1 = random.sample(range(1,30),10)
list2 = random.sample(range(1,30),10)
print(common(list1,list2))