def lol(l,a,s):
	for i in range(0,len(l)):
		if i == a:
			del l[i]
	if len(l) < s+1 :
		return l 
		
	a=l[a]
	for x in l:
		print(x, end=" ")
	print()
	
	lol(l,a-1,s)


s =int (input("enter you'r lucky number:"))
l=list()
for i in range(1,100):
	l.append(i)
'''for i in l:
	print(i, end=" ")
print()'''
a =1
lucky = lol(l,a,s)
for i in l:
	print(i,end=" ")

