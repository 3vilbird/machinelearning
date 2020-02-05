
a = int(input("enter the number:"))

for i in range(0,a):
	for j in range(0,i):
		print(" * ",end="")
	print()
for i in range(a-2,-1,-1):
	for j in range(0,i):
		print(" * ",end="")
	print()

