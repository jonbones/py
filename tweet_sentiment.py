#Jonathan S. Chandranathan
#Uses a given Twitter feed & a term-weighted dictionary to calculate the sentiment of each Tweet.

import sys
import json

global scores

def set_sentiment():
	global scores
	sent_file = open(sys.argv[1])
	scores = {}
	for line in sent_file:
		word, score = line.split("\t")
		scores[word] = int(score)
	sent_file.close()

def set_tweets():
	tweet_file = open(sys.argv[2])
	data = []
	tweets = []
	value = 0
	for line in tweet_file:
		t = json.loads(line)
		#if t.get("lang") == "en":
		data.append(t.get("text"))
	for line in data:
		for word in line.split():
			if word.encode('utf-8') in scores.keys(): value = value + scores[word]
		print value
		value = 0
	tweet_file.close()

set_sentiment()
set_tweets()
