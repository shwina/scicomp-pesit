from pylab import *
from scitools.easyviz import movie

x, y, t, T = loadtxt('x.txt'), loadtxt('y.txt'), loadtxt('t.txt'),\
			 loadtxt('T.txt')

def make_movie():

	for i in range(len(t)):
		temp = T[i, :]
		lev = linspace(50,150,21)
		contourf(x, y, reshape(temp, shape(x)),levels=lev,extend='both')
		savefig('img_%04d.png'%i)

	movie('*.png')

def make_contour(x, y, T):
	lev = linspace(50,150,11)
	c = contour(x, y, reshape(T[-1,:],shape(x)),colors='k',levels=lev)
	clabel(c)
	savefig('contour.png')

make_movie()
make_contour(x,y,T)
