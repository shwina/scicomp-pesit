
# A simple function

def silly_multiply(a, b):

	''' Multiply a and b using the tried-and-tested
		'repeated addition' method '''

	product = 0
	for i in range(a):		
		product += b	# i += j is the same as i = i + j
	
	return product	

# Returning multiple values

def minmax(a_list):
	
	minimum = min(a_list)
	maximum = max(a_list)

	return minimum, maximum


# Gathering arguments and passing a function to a function:

def timer(f, *args):
	
	''' Time the execution of a function f, which
		takes arguments listed in *args '''
	
	import time
	t1 = time.clock()
	f(*args)
	t2 = time.clock()
	
	return t2 - t1

print '%1.4f'%timer(silly_multiply, 4, 1000000)
print '%1.4f'%timer(silly_multiply, 1000000, 4)




