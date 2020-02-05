import sys
import numpy as n
import random


li=([(1,2,3,4,5,6),(1,2,3,4,5,6)])
lol= n.array(li)

'''
print(lol)
print(lol.shape,lol.dtype)

print(lol.size)
print(len(lol))
for i in lol:
	for j in i:
		print(j,end="   ")
	print()
lol.astype(float)
print(lol.dtype)
dd= n.array([1,2,3,4,5,6,7,8,9],dtype=complex)
print(dd)
#dimension
print("dimension",dd.ndim)
print("######"*10)
s=range(1000)
print(sys.getsizeof(s)*len(s))
ss=n.arange(1000);print(ss.size*ss.itemsize)
ga= n.zeros((2,3))
print(ga)
gg =n.ones((2,6),dtype=float)
print(gg)
sd = n.full((3,5),6)
print(sd)
#digonal elements are ones
eye =n.eye(4,4)
print(eye)
'''
a=n.array ([(1,2,3),(1,2,3)])
b=n.array ([(4,5,6),(1,2,3)])
print(n.vstack((a,b) ))
print(n.hstack((a,b) ))
print(a.ravel())
print(a.itemsize)
print(a.size)
#reshape of an array
a=a.reshape(3,2)
print(a)
#printing ppericular element
print(b[0:,2])

#linespacing to divide the given range
print(n.linspace(1,3,10))

#axis sum axis =0 sum of columns ,axis =1 sum of rows
print(a.sum(axis=0))
print(a.sum(axis=1))

#square root and standard deviation
print(n.sqrt(b)) 
print(n.std(b)) 

print(n.arange(64).reshape(4,4,4))
print(n.ones(64).reshape(4,4,4))

#random number generator
r=n.random.random((3,3))
print(r)
print(n.exp(r))
print(n.log(r))
print(n.log10(r))
print("$$$"*10)
x = n.array([1,1,2])
y = n.array([2,1,0])
print(n.cov(x,y))
print(n.all(y)) # test none of the elements  in the array are zero
print(n.all(x)) # test none of the elements  in the array are zero
