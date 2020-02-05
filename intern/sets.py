import itertools 
'''s=list(s)
for i in range(0,len(s)):
	d =  list()
	for x in range(0,i):
		d.append(s[x])
	print(set(d))
'''

# def findsubsets(s, n): 
def findsubsets(s, n): 
	for j in range(0,n):
		print ([set(i) for i in itertools.combinations(s, j)]) 
      
# Driver Code 
s = {1,2,3,4,5,6,7,10,12,9,13,15}
print(s)

n = len(s)
  
print(findsubsets(s, n)) 
		