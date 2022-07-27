import pandas as pd # se importa panda
import time # se importa la libreria de tiempo para realizar backups del exel

def agregar_usuario(nid,nusuario,npuntos,ndiscriminator,nmensaje):# la n es de nuevo
	exel=pd.read_excel("Datos_estudiantes.xlsx")#aca poner nombre del archivo que usemos
	cid=exel.columns[1]#se guarada el nombre de la columna, para despues volver a armar el exel #la c es de columna
	cus=exel.columns[2]#se guarada el nombre de la columna, para despues volver a armar el exel #la c es de columna
	cpu=exel.columns[3]#se guarada el nombre de la columna, para despues volver a armar el exel #la c es de columna
	cdi=exel.columns[4]#se guarada el nombre de la columna, para despues volver a armar el exel  #la c es de columna
	cme=exel.columns[5]#se guarada el nombre de la columna, para despues volver a armar el exel  #la c es de columna
	listid=[]#se guardan todos los valores de id en lista, para despues volver a armer el exel
	listus=[]#se guardan todos los valores de usuario en lista, para despues volver a armer el exel
	listpu=[]#se guardan todos los valores de punto en lista, para despues volver a armer el exel
	listdi=[]#se guardan todos los valores de mensaje en lista, para despues volver a armer el exel
	listme=[]#se guardan todos los valores de discriminator en lista, para despues volver a armer el exel
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listid.append(row[1])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listus.append(row[2])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listpu.append(row[3])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listdi.append(row[4])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listme.append(row[5])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	listid.append(nid)#se agregan los nuevos datos
	listus.append(nusuario)#se agregan los nuevos datos
	listpu.append(npuntos)#se agregan los nuevos datos
	listdi.append(int(ndiscriminator))#se agregan los nuevos datos
	listme.append(nmensaje)#se agregan los nuevos datos

	nexel=pd.DataFrame({cid:listid,cus:listus,cpu:listpu, cdi:listdi,cme:listme})#se arma el exel con las modificaciones

	archivo=pd.ExcelWriter("Datos_estudiantes.xlsx")#se abre el archivo para escribir #aca poner nombre del archivo que usemos

	nexel.to_excel(archivo,"Hoja1")# se escribe en el archivo y nombra la hoja en la que escribe como "Hoja1"

	archivo.save()#se guarda el archivo !!!!!no sacar porque se rompe el archivo !!!!!!!

	print("Se han guardados los cambios") # despues se puede cambiar para que el bot mande el mensaje

def cambiar_puntos(idi,imensaje):#idi =  interacion discriminador # imensaje = interaccion mensaje
	#posible comparacion del mansaje para filtrar letras solitarias y emojis 
	exel=pd.read_excel("Datos_estudiantes.xlsx")#aca poner nombre del archivo que usemos
	cid=exel.columns[1]#se guarada el nombre de la columna, para despues volver a armar el exel #la c es de columna
	cus=exel.columns[2]#se guarada el nombre de la columna, para despues volver a armar el exel #la c es de columna
	cpu=exel.columns[3]#se guarada el nombre de la columna, para despues volver a armar el exel #la c es de columna
	cdi=exel.columns[4]#se guarada el nombre de la columna, para despues volver a armar el exel  #la c es de columna
	cme=exel.columns[5]#se guarada el nombre de la columna, para despues volver a armar el exel  #la c es de columna
	listid=[]#se guardan todos los valores de id en lista, para despues volver a armer el exel
	listus=[]#se guardan todos los valores de usuario en lista, para despues volver a armer el exel
	listpu=[]#se guardan todos los valores de punto en lista, para despues volver a armer el exel
	listdi=[]#se guardan todos los valores de discriminator en lista, para despues volver a armer el exel
	listme=[]#se guardan todos los valores de mensaje en lista, para despues volver a armer el exel
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listid.append(row[1])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listus.append(row[2])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listpu.append(row[3])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listdi.append(row[4])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listme.append(row[5])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	i=True
	listo=False

	for x in range(0,(len(listdi))):#linea 55,56,57 y 58 para encontrar el discriminador del usuario que escribo y sumarle el puntaje

		if int(idi) == (int(listdi[x])):
			
			i=False
			j=x # guardo el subindice, que va a coincidir con todos los datos del usuario
			
	if i==True:
		print("Error 404 Discriminator no encontrado")
	if i==False:
		listpu[j]=listpu[j]+1 # se suma el puntaje # se puede cambiar despues
		listme[j]=str(listme[j])+"-"+imensaje # se agrega el nuevo mensaje
		listo=True # esto es para verificar que se realizo lo anterior
	if listo==True:
		nexel=pd.DataFrame({cid:listid, cus:listus, cpu:listpu, cdi:listdi,cme:listme})#se arma el exel con las modificaciones
		archivo=pd.ExcelWriter("Datos_estudiantes.xlsx")#se abre el archivo para escribir #aca poner nombre del archivo que usemos
		nexel.to_excel(archivo,"Hoja1")# se escribe en el archivo y nombra la hoja en la que escribe como "Hoja1"
		archivo.save()#se guarda el archivo !!!!!no sacar porque se rompe el archivo !!!!!!!
		print("Se han sumados los puntos") # despues se puede cambiar para que el bot mande el mensaje
	else:
		print("No se pudo sumar los puntos")# despues se puede cambiar para que el bot mande el mensaje

def backup():
	exel=pd.read_excel("Datos_estudiantes.xlsx")#aca poner nombre del archivo que usemos
	cid=exel.columns[1]#se guarada el nombre de la columna, para despues volver a armar el exel #la c es de columna
	cus=exel.columns[2]#se guarada el nombre de la columna, para despues volver a armar el exel #la c es de columna
	cpu=exel.columns[3]#se guarada el nombre de la columna, para despues volver a armar el exel #la c es de columna
	cdi=exel.columns[4]#se guarada el nombre de la columna, para despues volver a armar el exel  #la c es de columna
	cme=exel.columns[5]#se guarada el nombre de la columna, para despues volver a armar el exel  #la c es de columna
	listid=[]#se guardan todos los valores de id en lista, para despues volver a armer el exel
	listus=[]#se guardan todos los valores de usuario en lista, para despues volver a armer el exel
	listpu=[]#se guardan todos los valores de punto en lista, para despues volver a armer el exel
	listdi=[]#se guardan todos los valores de mensaje en lista, para despues volver a armer el exel
	listme=[]#se guardan todos los valores de discriminator en lista, para despues volver a armer el exel
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listid.append(row[1])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listus.append(row[2])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listpu.append(row[3])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listdi.append(row[4])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	for index, row in exel.iterrows():#el index es el subindice, y row es la fila 
		listme.append(row[5])#se llenan con los datos de las columnas #los numeros estan relacionados con los numbres de las columnas
	nexel=pd.DataFrame({cid:listid,cus:listus,cpu:listpu, cdi:listdi,cme:listme})#se arma el exel con las modificaciones
	tiempo_cadena = time.strftime("%d-%m-%Y")#facha local dia, mes, año
	nombre="backup_"+(str(tiempo_cadena))+".xlsx"#se le suma el formato del archivo
	archivo=pd.ExcelWriter(nombre)#se crea un archivo con nombre de la fache con formato xlsx
	nexel.to_excel(archivo,"Hoja1")# se escribe en el archivo y nombra la hoja en la que escribe como "Hoja1"
	archivo.save()#se guarda el archivo !!!!!no sacar porque se rompe el archivo !!!!!!!
	print("Se ha realizado una copia de seguridad")# despues se puede cambiar para que el bot mande el mensaje