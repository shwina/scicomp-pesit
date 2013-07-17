from twitter import *

#t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
#                       CONSUMER_KEY, CONSUMER_SECRET))

t = Twitter(auth=OAuth("18509049-R4GD9CggrJRZ646rgdnio3bqmevW7qF36formvaN1", "gGXDBo75pJ6dzuQXYmbMlrsUMoe1CNmUK9qex1iYA",
                       "YsH6mXYNhLq5Ycyj2ik70A", "aW1yqHWxPp2UL99P8akzCKm6tT3LHIA5eezS8zr6AQ"))


file = open("datafile.txt", "w")


search = t.search.tweets(q = 'Premium Rush', count = 100)
i = 1
for status in search['statuses']:
	file.write(str(i) + ". " + str(status['text'].encode('utf-8')) + "\n")
	i += 1

file.close()
