from spotipy.oauth2 import SpotifyClientCredentials
import spotipy, sys, time
import webbrowser as web
import pyautogui
from time import sleep
from datetime import datetime
from reproduccion import reproduccion
from cerrado import cerrado

def horarios():
	#escritura de las horas en un archivo
	tiempo_local_procesado=["0","0","0"]#definoi vaariable como lista vacia
	#test_tiempo=open("test tiempo.txt","w")#abro el archivo test tiempo.txt en modo escribir
	tiempo_local_completo=datetime.now()#pido la hora local
	#test_tiempo.write("Tiempo local completo \n")#escribo en el archivo
	#test_tiempo.write(str(tiempo_local_completo))#escribo la lista como str en el archivo
	#test_tiempo.write("\nTiempo local procesado\n")#escribo en el archivo
	tiempo_local_procesado[0]=tiempo_local_completo.hour#en el subindice 0 coloco solo la hora
	tiempo_local_procesado[1]=tiempo_local_completo.minute#en el subindice 1 coloco solo los minutos
	tiempo_local_procesado[2]=tiempo_local_completo.second#en el subindice 2 coloco solo los segundos
	#test_tiempo.write(str(tiempo_local_procesado))#escribo la hora procesada en el txt
	#test_tiempo.close()#cierro el archivo
	return tiempo_local_procesado

def hora1():#inicio recreo desayuno
	armado=["0","0","0"]
	archivo=open("tiempoh/desayuno1.txt","r")
	primerlinea=archivo.readline()
	
	print(f"primerlinea es:{primerlinea}")
	print(f"primerlinea es:{primerlinea[-4]}")
	print(f"primerlinea es:{primerlinea[-3]}")
	armado[2]=primerlinea[-4]+primerlinea[-3]
	armado[1]=primerlinea[-8]+primerlinea[-7]
	armado[0]=primerlinea[-12]+primerlinea[-11]
	print(f"armado tiene dentro: {armado}")
	archivo.close()
	return armado
def hora2():#final recreo desayuno
	armado=["0","0","0"]
	archivo=open("tiempoh/desayuno2.txt","r")
	primerlinea=archivo.readline()
	
	print(f"primerlinea es:{primerlinea}")
	print(f"primerlinea es:{primerlinea[-4]}")
	print(f"primerlinea es:{primerlinea[-3]}")
	armado[2]=primerlinea[-4]+primerlinea[-3]
	armado[1]=primerlinea[-8]+primerlinea[-7]
	armado[0]=primerlinea[-12]+primerlinea[-11]
	print(f"armado tiene dentro: {armado}")
	archivo.close()
	return armado
def hora3():#inicio recreo 1
	armado=["0","0","0"]
	archivo=open("tiempoh/recreo1.txt","r")
	primerlinea=archivo.readline()
	
	print(f"primerlinea es:{primerlinea}")
	print(f"primerlinea es:{primerlinea[-4]}")
	print(f"primerlinea es:{primerlinea[-3]}")
	armado[2]=primerlinea[-4]+primerlinea[-3]
	armado[1]=primerlinea[-8]+primerlinea[-7]
	armado[0]=primerlinea[-12]+primerlinea[-11]
	print(f"armado tiene dentro: {armado}")
	archivo.close()
	return armado
def hora4():#final recreo 1
	armado=["0","0","0"]
	archivo=open("tiempoh/recreo2.txt","r")
	primerlinea=archivo.readline()
	
	print(f"primerlinea es:{primerlinea}")
	print(f"primerlinea es:{primerlinea[-4]}")
	print(f"primerlinea es:{primerlinea[-3]}")
	armado[2]=primerlinea[-4]+primerlinea[-3]
	armado[1]=primerlinea[-8]+primerlinea[-7]
	armado[0]=primerlinea[-12]+primerlinea[-11]
	print(f"armado tiene dentro: {armado}")
	archivo.close()
	return armado
def hora5():#inicio almuerzo
	armado=["0","0","0"]
	archivo=open("tiempoh/almuerzo1.txt","r")
	primerlinea=archivo.readline()
	
	print(f"primerlinea es:{primerlinea}")
	print(f"primerlinea es:{primerlinea[-4]}")
	print(f"primerlinea es:{primerlinea[-3]}")
	armado[2]=primerlinea[-4]+primerlinea[-3]
	armado[1]=primerlinea[-8]+primerlinea[-7]
	armado[0]=primerlinea[-12]+primerlinea[-11]
	print(f"armado tiene dentro: {armado}")
	archivo.close()
	return armado
def hora6():#fin almuerzo
	armado=["0","0","0"]
	archivo=open("tiempoh/almuerzo2.txt","r")
	primerlinea=archivo.readline()
	
	print(f"primerlinea es:{primerlinea}")
	print(f"primerlinea es:{primerlinea[-4]}")
	print(f"primerlinea es:{primerlinea[-3]}")
	armado[2]=primerlinea[-4]+primerlinea[-3]
	armado[1]=primerlinea[-8]+primerlinea[-7]
	armado[0]=primerlinea[-12]+primerlinea[-11]
	print(f"armado tiene dentro: {armado}")
	archivo.close()
	return armado
def hora7():#inicio recreo 2
	armado=["0","0","0"]
	archivo=open("tiempoh/recreo3.txt","r")
	primerlinea=archivo.readline()
	
	print(f"primerlinea es:{primerlinea}")
	print(f"primerlinea es:{primerlinea[-4]}")
	print(f"primerlinea es:{primerlinea[-3]}")
	armado[2]=primerlinea[-4]+primerlinea[-3]
	armado[1]=primerlinea[-8]+primerlinea[-7]
	armado[0]=primerlinea[-12]+primerlinea[-11]
	print(f"armado tiene dentro: {armado}")
	archivo.close()
	return armado
def hora8():#fin recreo 2
	armado=["0","0","0"]
	archivo=open("tiempoh/recreo4.txt","r")
	primerlinea=archivo.readline()
	
	print(f"primerlinea es:{primerlinea}")
	print(f"primerlinea es:{primerlinea[-4]}")
	print(f"primerlinea es:{primerlinea[-3]}")
	armado[2]=primerlinea[-4]+primerlinea[-3]
	armado[1]=primerlinea[-8]+primerlinea[-7]
	armado[0]=primerlinea[-12]+primerlinea[-11]
	print(f"armado tiene dentro: {armado}")
	archivo.close()
	return armado
def hora9():#inicio merianda
	armado=["0","0","0"]
	archivo=open("tiempoh/merienda1.txt","r")
	primerlinea=archivo.readline()
	
	print(f"primerlinea es:{primerlinea}")
	print(f"primerlinea es:{primerlinea[-4]}")
	print(f"primerlinea es:{primerlinea[-3]}")
	armado[2]=primerlinea[-4]+primerlinea[-3]
	armado[1]=primerlinea[-8]+primerlinea[-7]
	armado[0]=primerlinea[-12]+primerlinea[-11]
	print(f"armado tiene dentro: {armado}")
	archivo.close()
	return armado
def hora10():#final merienda
	armado=["0","0","0"]
	archivo=open("tiempoh/merienda2.txt","r")
	primerlinea=archivo.readline()
	
	print(f"primerlinea es:{primerlinea}")
	print(f"primerlinea es:{primerlinea[-4]}")
	print(f"primerlinea es:{primerlinea[-3]}")
	armado[2]=primerlinea[-4]+primerlinea[-3]
	armado[1]=primerlinea[-8]+primerlinea[-7]
	armado[0]=primerlinea[-12]+primerlinea[-11]
	print(f"armado tiene dentro: {armado}")
	archivo.close()
	return armado
