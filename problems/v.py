
import string

# Open the file:

f = open('v.txt')
words = f.read()


''' Prepare a list of all words beginning with the
	letter 'V' (all lowercase). Call the list 'vlist' '''

# YOUR CODE HERE:
#---------------------------------------------------------------------------
deletechars = string.punctuation
words = words.translate(None, deletechars)
words = words.lower()
words = words.split()

vlist = []
for i in range(len(words)):	
	if words[i][0] == 'v':
		vlist.append(words[i])

#---------------------------------------------------------------------------

from pylab import *

vlengths = []
for i in range(len(vlist)):
	vlengths.append(len(vlist[i]))

his, bins = histogram(vlengths, bins=range(12))
print his, bins
#stem(bins, his)
show()
