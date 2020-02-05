s = int(input("Enter the input:"))
dd = list()
for i in range(0,s+1):
 	dd.append(i)

 #poping of 3rd element
print(dd)

for i in range(2,len(dd) ,2):
 	
 	if i >len(dd):
 		break
 	else:	
 		print(dd.pop(i))
 	
 	
 	


