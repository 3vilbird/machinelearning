def hcf(a,b):
	if b == 0:
		return a
	return hcf(b,a%b)

a = int(input("value for a: "))
b = int(input("value for b: "))
s = hcf(a,b)
print("hcf = "+str(s))
d = (a*b)/s
print("lcm = "+str(d))