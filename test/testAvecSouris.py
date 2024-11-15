import logging
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

"""
def on_mouse_scroll(mouse_position_x, mouse_position_y, scroll_x_change, scroll_y_change):
    message = ""
    if scroll_x_change < 0:
        message = "User is scrolling to the left"
    elif scroll_x_change > 0:
        message = "User is scrolling to the right"
    if scroll_y_change > 0:
        message = "User is scrolling up the page"
    elif scroll_y_change < 0:
        message = "User is scrolling down the page"

    print(message)
    logging.debug(message)
    logging.debug(f"Scroll change deltas: {scroll_x_change}, {scroll_y_change}")
    """


def on_mouse_click(mouse_position_x, mouse_position_y, button, is_pressed):
    if button == mouse.Button.middle and is_pressed:
        message = "Middle mouse button pressed! It's special!"
    else:
        message = f"Mouse button pressed: {button} | Is pressed: {is_pressed}"

    print(message)
    logging.debug(message)


# Crée un listener pour la souris
mouse_listener = mouse.Listener(
    on_move=on_mouse_move,
    #on_scroll=on_mouse_scroll,
    on_click=on_mouse_click
)

# Démarre le listener
print("Starting the mouse listener, will be active for 5 seconds...")
mouse_listener.start()
time.sleep(5)  # Laisse le script dormir pendant 5 secondes
print("Time's up, stopping the mouse listener")
mouse_listener.stop()
mouse_listener.join()
