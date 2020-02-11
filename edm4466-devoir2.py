# coding : utf-8

import csv
import json
import requests

url = "http://jhroy.ca/uqam/lobby.json"

entetes = {
    "User-Agent":"Nicholas Pereira - 438/832-9015 : requête envoyée dans le cadre d'un cours de journalisme de données", 
    "From":"pereira.nicholas@courrier.uqam.ca"
}

req = requests.get(url,headers=entetes)

if req.status_code != 200:
    print("Ça ne marche pas")
    
# for registre in test:
#     if registre ["objet"] == ["limat"]:
#         print(objet)

# -------------------------------------------------------

#CETTE ÉTAPE ME PERMET D'AVOIR ACCÈS À TOUTES LES INFORMATIONS DU REGISTRE
# if req.status_code == 200:
#     print("Yé")
#     code = req.json()
#     print(code["registre"])

# -------------------------------------------------------

#if req.status_code == 200:
    #print("Yé")
    #code = req.json()
    #for raison in code:
        #if raison ["objet"] == ["limat"]:
            #print(raison)

# if req.status_code == 200:
#     print("Yé")
#     code = req.json()
#     n = 0
#     for raison in code:
#         n += 1
#         infos = code.split(",")
#         print(n, code[0])

# if req.status_code == 200:
#      print("Yé")
#      code = req.json()
#      #print(code["registre"])

#      for items in code:
#          print (items["objet"])

# if req.status_code != 200:
#     print("Ça ne marche pas")
#     code = req.json()
    
#     for numero in code["registre"]:
#         if numero["objet"] == ["limat"]:
#             print(numero)

# ----------------------------

if req.status_code == 200:
    print("Yé")
    code = req.json()
    for numero in code["registre"]:
        numero = ["comlog_id"]
        clientan = ["en_client_org_corp_nm"]
        clientfr = ["fr_client_org_corp_nm"]
        date = ["date_comm"]
        sujet = ["objet"]
        sujet2 = ["objet_autre"]
        institution = ["institution"]
        print(numero, clientan, clientfr, date, sujet, sujet2, institution)

# ----------------------------

#Je suis évidemment bien loin du résultat recherché. Je n'ai même pas été en mesure de trouver comment 
# accéder (et trier) les éléments dans une liste. En fait, j'ai l'impression que le problème réside
# dans le fait que je ne suis pas capable de passer du dictionnaire "registre" à une liste.

#Mon objectif était d'utiliser la formule suivante apprise lors du dernier cours en classe:

# req = requests.get(url,headers=entetes)
# if req.status_code != 200:
#     print("Ça ne marche pas")
# else:
#     toune = req.json()
#     titre = toune["titre"]
#     faceA = toune["bitstreams"]["racine"]["fils"][0]["formats"][0]["url"]
#     faceB = toune["bitstreams"]["racine"]["fils"][1]["formats"][0]["url"]
#     print(titre, faceA)
#     infos.append(n)
#     infos.append(nb)
#     infos.append(titre)
#     infos.append(faceA)
#         # ou possible de faire infos = [n, nb, titre, faceA]
#     print(infos)

# J'aurais ensuite fait le fichier csv en utilisant la formule suivante :

#        dead = open(fichier, "a")
#         obies = csv.writer(dead)
#         obies.writerow(infos)
#     print(req)
#         print(numero)

#Demande : serait-ce possible de revenir sur la façon de faire en classe?