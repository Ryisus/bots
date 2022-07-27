from spotipy.oauth2 import SpotifyClientCredentials
import sys, time
import webbrowser as web
import pyautogui
from time import sleep
from datetime import datetime
from reproduccion import reproduccion
from cerrado import *
from horarios import horarios
from horarios import *
#from horarios import hora2 spotipy
client_id="2740a67b875f49769c64c03331dc0052" #client de acceso a spotify
client_secret ="07e69e21ad054c4b9069eaab89e423ea"
author ="Soda Stereo"
song = "Soda Stereo".upper()


#str minutop
#str hora1,horap,hora2,hora3,hora4,hora5,minuto1,minuto2,minuto3,minuto4,minuto5,aux,horaf1,horaf2,horaf3,horaf4,horaf5,minutof1,minutof2,minutof3,minutof4,minutof5
# aca va lo de horario
#flag=0
#hora local
#print(hora2())
aux=hora1() #inicio recreo
hora1=int(aux[0])
minuto1=int(aux[1])

aux=hora2()#final recreo
horaf1=int(aux[0])
minutof1=int(aux[1])

aux=hora3()
hora2=int(aux[0])
minuto2=int(aux[1])

aux=hora4()
horaf2=int(aux[0])
minutof2=int(aux[1])

aux=hora5()
hora3=int(aux[0])
minuto3=int(aux[1])


aux=hora6()
horaf3=int(aux[0])
minutof3=int(aux[1])

aux=hora7()#final recreo
hora4=int(aux[0])
minuto4=int(aux[1])

aux=hora8()
horaf4=int(aux[0])
minutof4=int(aux[1])

aux=hora9()
hora5=int(aux[0])
minuto5=int(aux[1])

aux=hora10()
horaf5=int(aux[0])
minutof5=int(aux[1])
print("hora 3:")
print(hora3)
print("hora f3:")
print(horaf3)
aux3=0
while 1:
	aux=horarios()
	horap=aux[0]
	minutop=aux[1]
	print(f"horap:{horap}")
	print(f"minutop:{minutop}")
	print("ante slep")
	sleep(20)
	print("despues slep")
	
	print("antes primer if")
	if((horap>=hora1)&(horap<=horaf1)):#horaf hora final
		print("primer if hora")
		if((minutop>=minuto1)&(minutop<minutof1)):
			print("dentro primer if")
			reproduccion()
			aux3=0
			while(aux3 !=1):
				aux=horarios()
				minutop=aux[1]
				if(minutop==minutof1):
					cerrado()
					aux3=1
					
	print("ante segundo if")
	if(horap>=hora2)&(horap<=horaf2):#horaf hora final
		print("segundo if hora")
		if(minutop>=minuto2)&(minutop<minutof2):#minutof minutof inal
			print("segundo if")
			reproduccion()
			aux3=0
			while(aux3!=1):
				aux=horarios()
				minutop=aux[1]
				if(minutop==minutof2):
					cerrado()
					aux3=1

	print("ante tercer if")
	if(horap==hora3)&(minutop==minuto3):
		print("tercer if")
		reproduccion()
		aux3=0
		while (aux3!=1):
			aux=horarios()
			horap=aux[0]
			minutop=aux[1]
			if(horap==horaf3)&(minutop==minutof3):
				cerrado()
				aux3=1

	print("ante cuarto if")
	if(horap>=hora4)&(horap<=horaf4):#horaf hora final
		print("cuarto if hora")
		if(minutop>=minuto4)&(minutop<minutof4):#minutof minutof inal
			print("cuarto if")
			reproduccion()
			aux3=0
			while(aux3!=1):
				aux=horarios()
				minutop=aux[1]
				if(minutop==minutof4):
					cerrado()
					aux3=1

	print("ante quinto if")
	if(horap>=hora5)&(horap<=horaf5):#horaf hora final
		print("quinto if hora")
		if(minutop>=minuto5)&(minutop<minutof5):#minutof minutof inal   $11 >=  $10    & $11 <=    $20 true
			print("quinto if")
			reproduccion()
			aux3=0
			while(aux3!=1):
				aux=horarios()
				minutop=aux[1]
				if(minutop==minutof5):
					cerrado()
					aux3=1
	print("funciono1")		


#hora=horap()
#horap=hora[-11] #-11 da la hora
#print(horap)
#busca en spotify el contenido la variable, en este caso soda stereo
#print(result)
#spotipy.client.SpotifyException(http_status, code, msg, reason=None, headers=None)

#aca se ejecutaria lo de la libreria reproduccion .py
#reproduccion()
#aca iria el cerrado
