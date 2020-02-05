f=input("enter the first input [format:dd/mm/yy]:")
l=input("enter the second input [format:dd/mm/yy]:")
f = f.list("/")
l = l.list("/")
m= [31, 28, 31, 30, 31, 30,  31, 31, 30, 31, 30, 31 ]
day =0
for i in range(f[0]+1,l[0]):
	if ((i%4==0 and i%100 !=0) or (i%400==0)):
		day = 366
	else:
		day= 365
# rectifying months
for x in range(f[1]+1,l[1]):
	day +=m[x]


	



