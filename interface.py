import string
from random import random

print("")

systemeExploitation = int(input("Êtes-vous sur windows ou linux ? Tapez 1 pour windows ou 2 pour linux"))

while(systemeExploitation!=1 & systemeExploitation!=2):
    systemeExploitation = int(input("Veuillez choisir 1 pour windows ou 2 pour linux"))

genereMail = int(input("Voulez-vous recevoir le fichier txt sur votre mail personnel ou bien voulez-vous générer un mail pour le recevoir dessus ? Tapez 1 pour choisir votre mail personnel ou 2 pour générer un mail"))
if genereMail == 1:
    mail = str(input("Veuillez écrire votre mail : "))
    # Envoyer le mail vers keylogger.py
else:
    # Generer un mail
    suffixLength=10
    generatedSuffix = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(suffixLength))