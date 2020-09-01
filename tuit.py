import json
import tweepy
# Enter your keys/secrets as strings in the following fields
credentials = {
        "CONSUMER_KEY": "KKg701T9QUlTTHGDaauKlTcKd",
        "CONSUMER_SECRET": "X1AyLTprCPrzTKqHIbBD67nTTMNmF95ajbNzud43BRbCTPdbJ0",
        "ACCESS_TOKEN": "470077550-oXR3ABFuGuBoSPUG1MpchJiSGJaIwVfkTd5Q3Eop",
        "ACCESS_SECRET": "O6UsaobBhWAD9Tt8B5b4QI2kdKeBFXnCqvQa30HTp6P82"
        }


auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_SECRET"])

api = tweepy.API(auth)

def get_tweets_by_id(user_id):
    user_tweets = api.user_timeline(user_id)
    return user_tweets

alexelcapo_tweets = get_tweets_by_id("EvilAFM")
for tweet in alexelcapo_tweets:
        print(tweet.text)
