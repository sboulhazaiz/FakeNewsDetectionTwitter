def DetectHTcomplot(api, user):
    liste_ht = '%23GrandRemplacement OR %23Soros OR %23BushDid911 OR %23ChinaDidCovid OR %23ChinaDidCovid19 OR %23pizzagates'

    tweetsUserLouche = api.GetSearch(raw_query='f=tweets&l=fr&q={(from:'+user+') ('+liste_ht+')}', include_entities=True)
    return tweetsUserLouche

    #RESTE A FAIRE : CONCATENER CETTE LISTE DE HT (la compléter peut-être) A UNE REQUETE DE RECHERCHE, EN Y INCLUANT LES ABONNEMENTS
    #CE QU'ON VA FAIRE C UN SYSTEME DE POINT GENRE UN POINT GAGNE PAR TWEET SUR HT LOUCHE ET UN DIXIEME DE PT OU MOINS GAGNE PAR COMPTE QUE LE MEC SUIT
    #et qui A tweeté sur des ht fumeux, le tout peut etre ramné au nb tweet pcq sinon biaisé pour les gens qui ont juste énormément de tweet ou d'abo
