#!/usr/bin/env python

#use the twitter module to find search trends
import twitter
twitter_search = twitter.Twitter(domain="search.twitter.com")
trends = twitter_search.trends()
[ trend['name'] for trend in trends['trends'] ]

#page through the search results
search_results = []
for page in range(1,6):
	search_results.append(twitter_search.search(q="#prayforjapan", rpp=100, page=page))

#use json to print the data
import json
print json.dumps(search_results, sort_keys=True, indent=1)

#list comprehension
tweets = [ r['test'] \
	for result in search_results \
		for r in result['results'] ]

#calculate the lexical diversity of returned tweets
words = []
for t in tweets: 
	words += [ w for w in t.split() ]

len(words) # total words
len(set(words)) # unique words
1.0*len(set(words))/len(words) #lexical diversity
1.0*sum([ len(t.split()) for t in tweets ])/len(tweets) # avg words per tweet