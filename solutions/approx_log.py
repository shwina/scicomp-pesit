
'''	Write a function that computes, approximately, the
	logarithm of (1 + x). The function must take 'x' as
	an argument and return log(1 + x). '''


x = 0.1

def approx_log(x, n_iter):
	y = x - 1
	out = 0
	for i in range(1,n_iter):
		out += (1./i)*(y/(1.0+y))**i
	return out

print approx_log(1.1,100)