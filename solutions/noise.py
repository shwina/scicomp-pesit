from pylab import sin, exp, cos, linspace, plot, savefig, show
import random

def make_noisy(dat):
    ''' Add noise to data '''
    noise = [random.uniform(-0.1*dat[i], +0.1*dat[i]) for i in range(len(dat))]
    return noise + dat

x = linspace(0,1,100)
y = sin(exp(cos(x)))
plot(x,y); plot(x, make_noisy(y)); 
show()
savefig('noise.png')
