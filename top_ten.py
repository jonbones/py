#Jonathan S. Chandranathan
#Scraping for hash tags.  Would like to turn this into a way to search for most popular hash tags within a given state.
#Could be used in conjunction with a sentiment analysis see how different areas in the US feel about different political buzzwords.

import sys
import json

global scores

def top_ten():
	global scores
	tweet_file = open(sys.argv[1])
	data = []
	hashes = []
	hash_count = {}
	for line in tweet_file:
		t = json.loads(line)
		data.append(t.get("entities"))
	for line in data:
		if line and "hashtags" in line.keys():
			hashes.append(line["hashtags"])
	for each in hashes:
		for i in range(0,len(each)):
			tag = each[i]["text"].encode('utf-8')
			if tag in hash_count.keys():
				hash_count[tag] = hash_count[tag] + 1
			else:
				hash_count[tag] = 1
	for tags in hash_count:
		print str(tags) + " " + str(float(hash_count[tags]))
	tweet_file.close()

top_ten()
