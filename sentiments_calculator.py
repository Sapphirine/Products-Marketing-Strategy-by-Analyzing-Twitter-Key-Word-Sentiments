import json
import re

def main(file):
    values = browse()
    sentimentsArray = []
    with open(file) as tffile:
        for line in tffile:
            if line:
                tweet = json.loads(line)
                result, text = caculate_sent(tweet, values)
                sentiments.append(result)
    weight = 0.0
    for i in sentiments:
        weight += i
    print weight / len(sentiments)

if __name__ == '__main__':
    main(sys.argv[1])

def caculate_sent(tweets, values):
    text = ""
    result = 0.0
    if u'text' in tweet:
        utf8_text = tweets[u'text']
        text = utf8_text
        tokens = re.split('\s+', utf8_text.lower())
        for word in tokens:
            word = re.sub('\W', '', word)
            if word in values:
                result += values[word]
        result = min(6, score)
        result = max(-6, score)
        for word in tokens:
            word = re.sub('\W', '', word)
            if word not in values and len(word) > 3:
                values[word] = 0

    return result, text

def browse():
    weights = {}
    with open('sentiments.txt') as f:
        for line in f:
            toks = re.split('\s+', line.strip().lower()) 
            if len(toks) == 2:
                word = toks[0]
                word = re.sub('\W', '', word)
                weights[word] = float(toks[1])
    return weights
