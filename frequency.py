#Jonathan S. Chandranathan
#Create a list of all words in a given feed and keep track of how often they appear.

import sys
import json

global scores
global wordcount

def find_freq():
	global scores
	global wordcount
	tweet_file = open(sys.argv[1])
	scores = {}
	data = []
	wordcount = 0
	for line in tweet_file:
		t = json.loads(line)
		if t.get("text") and t.get("lang") == "en":
			data.append(t.get("text"))
	for line in data:
		for word in line.split():
			wordcount = wordcount + 1
			if word in scores.keys():
				scores[word] = scores[word] + 1
			else:
				scores[word] = 1
	for word in scores:
		finalcount = float(scores[word]*1.0/wordcount)
		print word + " " + str(finalcount)
	tweet_file.close()

find_freq()
