

import json
tweets = []


with open('uber1.json') as tf:
  i = 0
  j = 0
  for line in tf:
    if line:
      try:
        tweets.append(json.loads(line))
        tweet = tweets[i]
        #print tweet
        #print line
        if 'New York' in tweet['user']['location']:
          print line,
          j = j + 1
        i = i + 1
      except:
        pass

#print j
#print len(tweet)
