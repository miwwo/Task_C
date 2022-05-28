import re

tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'

# tweet = re.search(r'\w+', r'$$ What??')
# print(tweet)
# print(tweet.group())

tweet = re.sub('http\S+', '', tweet)
print(tweet)
result = re.findall(r'\w+[^\S+]\w+', tweet)
print(result)
ans = ' '.join(result)
print(ans)
# \S - один не пробельный символ

