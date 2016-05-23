from twitter import *
import sys
import indicoio

access_key = "734176927825682433-UPc1vYiJjO0B4Ux6kj3GwRFXgIA22sK"
access_secret = "PpMlpJ412wx87g34msMRdir2yqfaiDTB6P0WqOdrlMxUw"
consumer_key = "jRsDidUota8wzQOin3AmKS312"
consumer_secret = "fRWBT5mK9EXWaZiIJCLdAO9FpbfU71eT4IHuv41OxazTJCeUdC"

indicoio.config.api_key = "070ef4588cd091fb23e3a6c9727097ce"
twitter = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

query = twitter.search.tweets(q = sys.argv[1], count = 15)
count = 0
total = len(query["statuses"])
ratingsum = 0;
strings = []

for result in query["statuses"]:
        tweet = result["text"].encode(encoding='UTF-8',errors='strict') 
        weight = indicoio.sentiment_hq(tweet)
        print(weight)
        ratingsum += weight
        string = "@%s | https://twitter.com/%s/status/%s | %s\n" % (result["user"]["screen_name"], result["user"]["screen_name"], result["id_str"], tweet)
        if weight > 0.5:
                strings.append(string);
                count = count + 1;
print("The average favorability of tweets, with 1 being the most favorable, is %2f" % (ratingsum/total))
print("%s tweets with positive sentiment found that mention %s\n" % (count, sys.argv[1]))
print("twitter user | tweet link | tweet message")
for index in range(0, count):
        print(strings[index])
