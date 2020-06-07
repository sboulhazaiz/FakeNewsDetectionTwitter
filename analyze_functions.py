import sys
import time

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
    print('\n Ce compte follow '+str(taux)+'% de compte qui propagent des fake news')
    return taux
