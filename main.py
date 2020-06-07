import json
from json import JSONDecoder

import twitter

from time import sleep

from requests_oauthlib import OAuth1Session
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from auth import getoauth
from analyze_functions import DetectHTcomplot
from twitter_credentials import *

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

api = twitter.Api(application_only_auth=True, consumer_key=twitter_credentials.CONSUMER_KEY, consumer_secret=twitter_credentials.CONSUMER_SECRET, access_token_key=twitter_credentials.ACCESS_TOKEN, access_token_secret=twitter_credentials.ACCESS_TOKEN_SECRET)
#print(api.VerifyCredentials())
"""user = api.GetUser(screen_name='RebeuDeter')
print(user.name)"""
"""tweetsBillchien = api.GetUserTimeline(count=15)
print([s.text for s in tweetsBillchien])"""

#tweetsUserLouche = api.GetSearch(raw_query='f=tweets&l=fr&q={(from:joyeusespaques2) (%23KohLanta2020) OR (%23BlackLivesMatter)}', include_entities=True)
tweetsUserLouche = DetectHTcomplot(api, 'pierre_1er')
dec = JSONDecoder()
#print(tweetsUserLouche)
#tab = dec.decode(tweetsUserLouche)
# A REMETTRE print([s.text for s in tweetsUserLouche])
print(hashtags utilisés : )


#print(api.GetReplies('Elfion'))

#getter = GetTweet()
#getter.get_tweets()

