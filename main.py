import json
from json import JSONDecoder

import twitter_credentials
import twitter
import pprint
from time import sleep

from requests_oauthlib import OAuth1Session
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from analyze_functions import *
from twitter_credentials import *
from googleapiclient.discovery import build

api = twitter.Api(application_only_auth=True, consumer_key=twitter_credentials.CONSUMER_KEY,
                  consumer_secret=twitter_credentials.CONSUMER_SECRET,
                  access_token_key=twitter_credentials.ACCESS_TOKEN,
                  access_token_secret=twitter_credentials.ACCESS_TOKEN_SECRET)
api_OAuth1 = twitter.Api(application_only_auth=False, consumer_key=twitter_credentials.CONSUMER_KEY,
                         consumer_secret=twitter_credentials.CONSUMER_SECRET,
                         access_token_key=twitter_credentials.ACCESS_TOKEN,
                         access_token_secret=twitter_credentials.ACCESS_TOKEN_SECRET)

# api is for calling Twitter api through application-only authentification, while api_OAuth1 is for calling apis through OAuth1.0, some will work with either
# appication-only, or Oauth1.0 or with both !

# print(api.VerifyCredentials())
"""user = api.GetUser(screen_name='RebeuDeter')
print(user.name)"""
"""tweetsBillchien = api.GetUserTimeline(count=15)
print([s.text for s in tweetsBillchien])"""

# tweetsUserLouche = api.GetSearch(raw_query='f=tweets&l=fr&q={(from:joyeusespaques2) (%23KohLanta2020) OR (%23BlackLivesMatter)}', include_entities=True)

print('Select the feature to use (menu added soon - still in progress) : ')

print('Paste the tweet to analyze : ')
# lien_tweet = input()                    #type the URL of the tweet
lien_tweet = 'https://twitter.com/eksansk/status/1272170912360652800' #the algorithm is currently in tests so this tweet is forced in the algorithm everytime
id_tweet = lien_tweet.split("/")[5]  # tweet trim to keep only the ID of the tweet
obj_tweet = api.GetStatus(id_tweet)  # pull the tweet (as a JSON object)
scr_name = obj_tweet.user.screen_name  # get the @ of the user that tweeted this
print(scr_name)

# ----------------------------------------- ANALYZING THE AUTHOR
tweetsUserLouche = DetectHTcomplot(api, scr_name)  # détection si l'utilisateur a déjà tweeté sur des ht théorie complot
# A AJOUTER : PARCOURIR ABONNES DE L'USER ET LES SCANNER
# print(tweetsUserLouche)
# tab = dec.decode(tweetsUserLouche)
# A REMETTRE print([s.text for s in tweetsUserLouche])


# ----------------------------------------- ANALYZING TWEET ITSELF
filtered_tweet = filterkeywords(obj_tweet.text)  # sending the text tweet into my word filtering function
print("Scanning french fact checking websites")

results = google_search('La 5G propage le coronavirus', twitter_credentials.GOOGLE_API_KEY, twitter_credentials.GOOGLE_CSE_KEY_SITENEWS, num=10) # querying my google custom search engine that searches in factchecking website
                                                                 #to track if that news has already been marked as fake news
# for result in results:
#    pprint.pprint(result)
if isinstance(results, str): # if the var returned is a string it means the json returned was empty so no results
    print("no results on google")
else:
    print('fake news already debunked on google')
    with open('data.json', 'w') as outfile:
        json.dump(results, outfile)

# ----------------------------------------- ANALYZING FOLLOWEE'S AUTHOR

followees_object = api_OAuth1.GetFriends(screen_name="Beyonce") #currently under test so I had to force a screen_name of a twitter user with few followINGS
followees_array = []
i = 0
for followee in followees_object:
    followees_array.append(followee.screen_name)
    # print(followees_array[i]+' ---- i ='+str(i))
    # i+=1
taux_comptes_fakenews = FolloweesAnalysis(api, followees_array)

'''for entities in tweetsUserLouche:
	ht = entities.'''

if tweetsUserLouche == True:
    print('This user ever tweeted with fake news hashtags')
else:
    print("This user never tweeted with fake news hashtags")
