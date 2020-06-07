import json
from json import JSONDecoder

import twitter

from time import sleep

from requests_oauthlib import OAuth1Session
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from auth import getoauth
from analyze_functions import DetectHTcomplot, FolloweesAnalysis
from twitter_credentials import *

import twitter_credentials


api = twitter.Api(application_only_auth=True, consumer_key=twitter_credentials.CONSUMER_KEY, consumer_secret=twitter_credentials.CONSUMER_SECRET, access_token_key=twitter_credentials.ACCESS_TOKEN, access_token_secret=twitter_credentials.ACCESS_TOKEN_SECRET)
api_OAuth1 = twitter.Api(application_only_auth=False, consumer_key=twitter_credentials.CONSUMER_KEY, consumer_secret=twitter_credentials.CONSUMER_SECRET, access_token_key=twitter_credentials.ACCESS_TOKEN, access_token_secret=twitter_credentials.ACCESS_TOKEN_SECRET)

#api is for calling Twitter api through application-only authentification, while api_OAuth1 is for calling apis through OAuth1.0, some will work with either
#appication-only, or Oauth1.0 or with both !

#print(api.VerifyCredentials())
"""user = api.GetUser(screen_name='RebeuDeter')
print(user.name)"""
"""tweetsBillchien = api.GetUserTimeline(count=15)
print([s.text for s in tweetsBillchien])"""

#tweetsUserLouche = api.GetSearch(raw_query='f=tweets&l=fr&q={(from:joyeusespaques2) (%23KohLanta2020) OR (%23BlackLivesMatter)}', include_entities=True)

print('Entrez le lien du tweet à analyser : ')
#lien_tweet = input()                    #type the URL of the tweet
lien_tweet = 'https://twitter.com/anda_le_dada/status/1180807840522481665'
id_tweet = lien_tweet.split("/")[5]     # tweet trim to keep only the ID of the tweet
obj_tweet = api.GetStatus(id_tweet)     #pull the tweet (as a JSON object)
scr_name = obj_tweet.user.screen_name   #get the @ of the user that tweeted this

tweetsUserLouche = DetectHTcomplot(api, scr_name)
#A AJOUTER : PARCOURIR ABONNES DE L'USER ET LES SCANNER
#print(tweetsUserLouche)
#tab = dec.decode(tweetsUserLouche)
# A REMETTRE print([s.text for s in tweetsUserLouche])

followees_object = api_OAuth1.GetFriends(screen_name='Beyonce')
followees_array = []
i = 0
for followee in followees_object:
    followees_array.append(followee.screen_name)
    print(followees_array[i]+' ---- i ='+str(i))
    i+=1
taux_comptes_fakenews = FolloweesAnalysis(api, followees_array)


'''for entities in tweetsUserLouche:
    ht = entities.'''

if tweetsUserLouche == True:
    print('Cet user a tweeté sur des hashtag fake news')
else:
    print("cet user n'a pas tweeté sur des fnews")

