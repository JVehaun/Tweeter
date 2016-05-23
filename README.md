# Tweeter

This python script uses the twitter api to search for tweets, then uses the indico text sentiment api to analyze the favorability of each tweet. The script then returns the average favorability rating of the tweets as well as a list of the positive tweets back to the user.

Use with:
python tweeter.py "search term here"

#Examples

The following has overwhelmingly positive related tweets:
python tweeter.py "@GTMGH3"
python tweeter.py "@trustfuel"

Whereas the following has mixed tweets:
python tweeter.py "@HillaryClinton"
python tweeter.py "@realDonaldTrump"
