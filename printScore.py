words = open("words.txt", "r")
scores = {}
for line in words:
	word,score = line.split("\t")
	scores[word] = int(score)

print scores

#for word,score in scores.iteritems():
#	print str(word) + " has a score of:" + str(scores[word])
