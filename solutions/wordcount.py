import sys
import string
import numpy as np

def count_occurrence(f, s):
	''' count the number of occurrences of a string s in a text
		file f. '''

	words_in_file = f.read()
	words_in_file = string.lower(words_in_file)
	words_in_file = words_in_file.split()
	
	return words_in_file.count('python')

filenames = sys.argv[:]
target = 'python'
wordcounts = []

for name in filenames:	
	f = open(name, 'r')	
	wordcounts.append(count_occurrence(f, target))
	f.close()

indices = np.argsort(wordcounts)

for i in range(len(filenames)):
	print filenames[indices[i]], wordcounts[indices[i]]
