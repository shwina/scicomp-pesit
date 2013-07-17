import numpy.random as random
from matplotlib.pyplot import *

def one_or_two():
	r = random.randint(1,high=3)	# high is excluded, so 1 or 2
	return r

ntries = 100	# How many random walks
nsteps = 5000	# How many steps per random walk
posn = 0		# Initial position

for k in range(ntries):
	y = []
	posn = 0
	for i in range(nsteps):
		r = one_or_two()
		if r==1:
			posn += 1
		else:
			posn -= 1
		if i%10 == 0:	# Every few steps, add to plot
			y.append(posn)
	plot(np.linspace(1, nsteps, len(y)), y, 'k')
	xlabel('Steps')
	ylabel('Position')

show()
