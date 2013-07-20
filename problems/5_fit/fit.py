from numpy import *
from scipy.optimize import curve_fit
from matplotlib.pyplot import *

def model(x, c, m):
	return c*(1 + exp(-m*x))

x, y = loadtxt('x.txt'), loadtxt('y.txt')
plot(x,y,'o')
show()

params, covariance  = curve_fit(model, x, y)

c, m = params[0], params[1]

plot(x,y,'s')
plot(x,model(x, c, m))
show()
