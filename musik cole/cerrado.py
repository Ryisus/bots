from spotipy.oauth2 import SpotifyClientCredentials
import spotipy, sys, time
import webbrowser as web
import pyautogui
from time import sleep
from datetime import datetime

def cerrado():
	pyautogui.keyDown("alt")#mantiene la tecla presionada
	pyautogui.keyDown("f4")#mantiene la tecla presionada
	sleep(1)
	pyautogui.keyUp("alt")#deja de precionar la tecla
	pyautogui.keyUp("f4")#deja de precionar la tecl