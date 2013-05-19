#Jonathan S. Chandranathan
#Find the top ten most popular hash tags in a given feed sample.

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
	x = 0
	for tags in hash_count:
		if x < 10:
			print str(tags) + " " + str(float(hash_count[tags]))
		x = x + 1
	tweet_file.close()

top_ten()
