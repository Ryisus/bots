from spotipy.oauth2 import SpotifyClientCredentials
import spotipy, sys, time
import webbrowser as web
import pyautogui
from time import sleep
from datetime import datetime

def reproduccion():
    client_id="2740a67b875f49769c64c03331dc0052" #client de acceso a spotify
    client_secret ="07e69e21ad054c4b9069eaab89e423ea"
    author ="Soda Stereo"
    song = "Soda Stereo".upper()

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id,client_secret))# se loguea en la pagina
    #result = sp.search(author)


    flag=0
    #for i in range(0, len(result["tracks"]["items"])):
        # songs by artist
     #   name_song = result["tracks"]["items"][i]["name"].upper()

      #  if song in name_song:
       #     flag = 1
        #    web.open(result["tracks"]["items"][i]["uri"])
         #   sleep(5)
          #  pyautogui.press("enter")
           # break
    if flag == 0:#con esto abre y se mueve dentro de spotify
        song = song.replace(" ", "%20")#agrega una terminacion al nombre para la busqueda
        web.open(f'spotify:search:')#abre spotify y busca la cancion #search{}
        
    sleep(15)# espera en segundos

    for i in range(4):#el range es la cantidad de veces que va a apretar tabulador #agregar 11 #sumjado 29 #original 18 # 17 "funciona"
        pyautogui.press("tab")#preciona la tecla tabulador 5
        sleep(0.5)

    pyautogui.press("enter")
    sleep(0.5)

    for i in range (5):
        pyautogui.press("tab")
        sleep(0.5)

    sleep(2)#despues de que se precionen todas las veces tab espera 2 seg
    for i in range(1):#esto es la cantidad de veces que presiona la tecla enter # 1 solo para reproducir tema # 2 para reproducir y para
        pyautogui.press("enter")#preciona la ttecla enter
        sleep(1)#espera 1 seg
