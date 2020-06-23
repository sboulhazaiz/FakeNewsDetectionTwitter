import sys
import time
import re
from googleapiclient.discovery import build
import pprint

def DetectHTcomplot(api, user):
    liste_ht = '%23GrandRemplacement OR %23Soros OR %23BushDid911 OR %23ChinaDidCovid OR %23ChinaDidCovid19 OR %23pizzagates'

    tweetsUserLouche = api.GetSearch(raw_query='f=tweets&l=fr&q={(from:'+user+') ('+liste_ht+')}', include_entities=True)
    #print([s.text for s in tweetsUserLouche])
    if not tweetsUserLouche:
        return False
    if tweetsUserLouche:
        return True


    #RESTE A FAIRE : CONCATENER CETTE LISTE DE HT (la compléter peut-être) A UNE REQUETE DE RECHERCHE, EN Y INCLUANT LES ABONNEMENTS
    #CE QU'ON VA FAIRE C UN SYSTEME DE POINT GENRE UN POINT GAGNE PAR TWEET SUR HT LOUCHE ET UN DIXIEME DE PT OU MOINS GAGNE PAR COMPTE QUE LE MEC SUIT
    #et qui A tweeté sur des ht fumeux, le tout peut etre ramné au nb tweet pcq sinon biaisé pour les gens qui ont juste énormément de tweet ou d'abo

def FolloweesAnalysis(api, list_followees):
    fakenewser  = 0
    i = 0
    number_followees = len(list_followees)
    number_followees_str = str(number_followees)
    for followee in list_followees:
        if DetectHTcomplot(api, followee):
            fakenewser=+1
        i+=1
        sys.stdout.write("\r{0}".format('abonnements analysés : '+str(i)+'/'+number_followees_str)) #dynamic display of progression
        sys.stdout.flush()
        #print('abonnements analysés : '+str(i)+'/'+number_followees_str)
    taux = (fakenewser/number_followees)*100
    print('\n Ce compte follow %.2f'% taux +'% de compte qui propagent des fake news')
    return taux


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def filterkeywords (query): #filter the query to keep only the keywords
    stopwords = ['le', 'la', 'un', 'une', 'au', 'aux', 'les', 'pour', 'sur', '‼️'] #list of words to be filtered out (in french)
    querywords = query.split() #spliting the query in list of words
    resultwords  = [word for word in querywords if word.lower() not in stopwords] #filtering out the words
    result = ' '.join(resultwords) #
    result = text = re.sub(r'http\S+', '', result)
    return result

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    stopwords = ['le', 'la', 'un', 'une', 'au', 'aux', 'les', 'pour']
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    #nombre_res = res[searchInformation]
    if res['searchInformation']['totalResults'] != '0':
        return res['items']
    else:
        return "aucun résultat"