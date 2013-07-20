#-----------------------------------------------------------------------
# search
#  Does a few awesome things:
#    	- considers a search query for twitter
#	- obtains the first 1000 search results of the query
#       - gets the sentiment 'score' of all the words of each tweet
#		and stores it in totals[], IF the score is non-zero
#	- if the tweet is geotagged, stores the coordinates of 
#		origin of tweet in coordinates_list = []
#	- plots the histogram of scores
#	- plots the points of geotagged tweets on a world map
#	
#-----------------------------------------------------------------------


from twitter import *
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
 
# Lets make a worldmap 
map = Basemap(projection='robin', lat_0 = 0, lon_0=77.5833,
              resolution='l', area_thresh=1000.0)

# t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
#                       CONSUMER_KEY, CONSUMER_SECRET))

t = Twitter(auth=OAuth("18509049-R4GD9CggrJRZ646rgdnio3bqmevW7qF36formvaN1", "gGXDBo75pJ6dzuQXYmbMlrsUMoe1CNmUK9qex1iYA",
                       "YsH6mXYNhLq5Ycyj2ik70A", "aW1yqHWxPp2UL99P8akzCKm6tT3LHIA5eezS8zr6AQ"))

# Now lets get the list of words and their 'positivity' and 'negativity' and store it in a dictionary 'scores'
# The list is available at https://github.com/kenchang408/twitter-sentiment-python/blob/master/AFINN-111.txt
# read about the history and stuff here: https://github.com/kenchang408/twitter-sentiment-python/blob/master/AFINN-README.txt
f = open("words.txt", "r")
scores = {}

for line in f:
	#The words and their scores are tab separated
	word,score = line.split("\t")
	scores[word] = int(score)
f.close()

# Open a txt file to store all the tweets we will evaluate! 
f = open("Evaluated_tweets.txt","w")

# max_id funda here: https://dev.twitter.com/docs/working-with-timelines
max_id_str = 0

# Initiate the scores list 'totals[]' and coordinates list
# And we use tweet_num to number the tweets in Evaluated_tweets.txt 
totals = []
coordinates_list = []
tweet_num = 1

# This for loop is needed to search through 10 pages :D 
for i in range(1,11):

	# Now lets search for the tweets, the 'search' dictionary is a crazy dictionary 
	# count is the number of tweets per page, 100 is max
	search = t.search.tweets(q = 'Flight :(', count = 100,lang='en', max_id = max_id_str)
	for status in search['statuses']:
		total = 0
		
		# Get each tweet in the search		
		tweet = (str(status['text'].encode('ascii','replace')).strip('#'))
		
		# Get the coordinates, if they are there. 
		if status['geo']:		
			coordinates = status['geo']['coordinates']
		else:
			coordinates = [0,0]
		
		# Split da tweet
		all_da_words = tweet.split()
		
		# Get scores of each word, if the word happens to be words.txt
		for each_word in all_da_words:
			if each_word in scores:
				total += scores[each_word]
		
		# Do stuff with the non - zero scores, bro
		if total != 0:
			# Append some lists
			coordinates_list.append(coordinates)
			totals.append(total)

			# Write the data to a file 
			f.write(str(tweet_num) +". " + tweet + "\n" )
			f.write("\tcoordinates : " + str(coordinates) + "\n")
			f.write("\tscore is : " + str(total) + "\n\n") 
              		
			tweet_num += 1
	
	# Get the max_id of the search, so that we can use it for the next search!
	# If there are no more results to show, twitter removes the 'next_results' key from
	# the search['search_metadata'] dictionary, so lets go ahead and take care of that
	try:	
		max_id_str = search['search_metadata']['next_results'][8:26]
		print ("page " + str(i) +" done loading")
	except KeyError:
		print("No more results.. ")
		break		
	
# Print some stuff and make us happy
print "All Done!"
print " "

print "Score list :"
print totals
print " "

print "Corresponding coordinates list :"
print coordinates_list
print " "

# Lets make a list of the non - zero coordinates and print them too
coos_list = []
indices = []
for index,coos in enumerate(coordinates_list):
	if coos != [0,0] and coos not in coos_list:
		coos_list.append(coos)
		indices.append(index)

print "List of non-zero coordinates: "
print coos_list	
print " "

# Now lets print the number of tweets out of the 1000 that had words
# from our words.txt and were hence evaulated
print "Number of tweets evaluated : " + str(len(totals))

# Lets plot the histogram of the scores, to see if
# the world likes your query or not
plt.subplot(211)
plt.hist(totals)

# Lets also plot, where the geo-tagged tweets seem to originate from
plt.subplot(212)
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='coral')
#map.bluemarble()
map.drawmapboundary()
 
lons = []
lats = []

# Lets use coos_list to get our longitudes and latitudes
for coo in coos_list:
	lats.append(coo[0])
	lons.append(coo[1])

x,y = map(lons, lats)

# Lets plot the points with blue circles! :D
map.plot(x, y, 'bo', markersize=10)

# And now we grab some pop corn and wait.
plt.show()
