import time
import numpy as np

largest = 0

t1 = time.clock()

for i in range(100, 1000):
	for j in range(100, 1000):
		num = i*j
		if str(num) == str(num)[::-1]:
			if num > largest:		
				largest = num
print largest

t2 = time.clock()

print 'First algorithm found largest palindrome: ',largest,' in ' '%f'%(t2-t1), 'seconds'

largest = 0

t1 = time.clock()

k = 100
for i in range(100, 1000):
	for j in range(k,1000):
		num = i*j
		if str(num) == str(num)[::-1]:
			if num > largest:
				largest = num
	k+=1

t2 = time.clock()

print 'Second algorithm found largest palindrome: ',largest,' in ' '%f'%(t2-t1), 'seconds'


