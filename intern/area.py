def area(h,w):
	for i in range(0,h):
		print("*"*w)
	a = h*w
	print("area of the rectangle is   "+str(a))


h=int(input("enter the height and width:"))
w=int(input("enter the width:"))
area(h,w)
	

	