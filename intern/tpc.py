def cylender():
	r = float(input("enter the readius:"))
	h = float(input("enter the height:"))
	area = float((2*3.142*r*h)+(2*3.142*r**2))
	print("area   "+str(area))


def trapezoid():
	a= float(input("enter the base1:"))
	b= float(input("enter the base2:"))
	h= float(input("enter the height:"))
	area = float(((a+b)/2)*h)
	print("area   "+str(area))









print("enter the choice:\n 1.cylender \n 2.trapezoid")
s =int(input())

try:
	if s == 1:
		cylender()
	elif s == 2:
		trapezoid()



	
except:
	print("Invalid choice")
