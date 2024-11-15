import PIL.ImageGrab
import os

screen=PIL.ImageGrab.grab()
path = os.getcwd()
path +="/screen.png"
screen.save(path)
