import time
'''

for x in range(2500,5701):

	if x%7 == 0 and x%5 == 0 :
		print(x)
		print()
		time.sleep(.2)'''

print("caculating")
for i in range(1,10):
	print("="*i,end="")
	time.sleep(.5)
print("=>")
for x in range(1,52):
	if x%3==0 and x%5==0:
		print("fizzbuzz")
		#continue
	elif x%3==0:
		print("fizz")
	elif x%5 == 0:
		print("buzz")
	else:
		print(x)
print("#"*5)


	