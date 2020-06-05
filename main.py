import json
import twitter

from time import sleep

from requests_oauthlib import OAuth1Session
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from auth import getoauth

import twitter_credentials


class GetTweet:

    def __init__(self):
        pass

    def get_tweets(self):
        params = {"ids": "1268052291988238336", "tweet.fields": "created_at"}

        # This handles Twitter authetification and the connection to Twitter Streaming API
        #listener = StdOutListener(fetched_tweets_filename)

        #oauth = OAuth1Session()
        oauth = getoauth()

        response = oauth.get("https://api.twitter.com/labs/2/tweets", params = params)
        """print("Response status: %s" % response.status_code)
        print("Body: %s" % response.text)"""
        #print("2EME TWEET AVEC LE MEME TOKEN : ")

        #sleep(1)

        rep_format = json.loads(response)
        print("donnees : ")
        print(rep_format[0]['data']['text'])



        # CODER LA RECHERCHE DES NEWS DE L'INFO DE L'AUTRE CONNARD SUR GOOGLE POUR VOIR SI JE

        # a tenter : auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        # a tenter (suite): auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        #stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        #stream.filter(track=hash_tag_list)

print("TEST DEBUG")

consumer_key = 'hertAn2zPggjBwFf5W92bWPv8'  # Add your API key here
consumer_secret = '7AoLj0E0x6yR2YiA1bdyxnL7jG47INZCDyvl4VlC10rsgKVPXW'  # Add your API secret key here
token = '1228505037049094145-ZeEXdDPE7YLcOuXfQeuUcsmg3y4GbP'
token_secret = 'f9WLfejO2yUlGhyJnuUJ4RU9mU71XwXqSDsYhvSNd0nWG'

api = twitter.Api(application_only_auth=True, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=token, access_token_secret=token_secret)
#print(api.VerifyCredentials())
"""user = api.GetUser(screen_name='RebeuDeter')
print(user.name)"""
"""tweetsBillchien = api.GetUserTimeline(count=15)
print([s.text for s in tweetsBillchien])"""

tweetsUserLouche = api.GetSearch(raw_query='f=tweets&l=fr&q={(from:joyeusespaques2) (%23KohLanta2020) OR (%23BlackLivesMatter)}', include_entities=True)
print([s.text for s in tweetsUserLouche])

#print(api.GetReplies('Elfion'))

#getter = GetTweet()
#getter.get_tweets()

