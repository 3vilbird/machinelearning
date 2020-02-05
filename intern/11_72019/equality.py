import numpy as np 

a = np.array([1 ,0, 1, 0, 1, 1])

b =np.array([0,0,1,1,1,0])
print(a)
print(b)
#s = np.array_equal(a,b)
if np.array_equal(a,b) == 1:
	print("equal")
else:
	print("not equal")


print(np.allclose(a,b))	
print(np.random.randint(0,2,6))#print 0=starting 2=(total ie 0 or 1),6 =total generation
print("$"*8)


print("March, 2017")
print(np.arange('2017-03', '2017-04', dtype='datetime64[D]'))

# to get today, tommarow and yesterdays date 


'''
Basic Datetimes

The most basic way to create datetimes is from strings in ISO 8601 date or datetime format.
 The unit for internal storage is automatically selected from the form of the string, and can be either a date unit or a time unit.
  The date units are years (‘Y’), months (‘M’), weeks (‘W’), and days (‘D’), while the time units are hours (‘h’), minutes (‘m’), seconds (‘s’), milliseconds (‘ms’),
   and some additional SI-prefix seconds-based units.


'''

print(':::'*8)
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yestraday: ",yesterday)
today     = np.datetime64('today', 'D')
print("Today: ",today)
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)

