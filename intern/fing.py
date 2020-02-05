s = input("enter the sring :")
s=s.split()
print(s)
#print(s)
for x in s :
	if x.startswith('a') or x.startswith('e'):
		print(x)
