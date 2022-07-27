import pandas as pd
import time

def buscar_diccionario(mensaje):
	promen=mensaje.split(" ")
	print(promen)
	print(len(promen))
	for i in range(0, len(promen)-1):
		print(promen[i])
		print(i)
		repade=palabras_denegadas(promen[i])#return palabra denegadas
		if repade==True:
			promen.pop(i)
	exel=pd.read_excel(io="Diccionario.xlsx", sheet_name="Diccionario")
	exel2=pd.read_excel(io="Diccionario.xlsx", sheet_name="Nuevas_palabras")
	coldi=exel.columns[1]
	colnp=exel2.columns[1]
	listnp=[]
	listdic=[]
	for index, row in exel.iterrows():
		listdic.append(str(row[1]))
	for index, row in exel2.iterrows():
		listnp.append(str(row[1]))
	for i in range(0,len(promen)):
		palabra_en_mensaje=False
		for x in range(0,len(listdic)):
			if promen[i] == listdic[x]:
				palabra_en_mensaje=True
		if palabra_en_mensaje==False:
			listnp.append(promen[i])		
	nexel=pd.DataFrame({coldi:listdic})
	nexel2=pd.DataFrame({colnp:listnp})
	archivo=pd.ExcelWriter("Diccionario.xlsx")
	nexel.to_excel(archivo,sheet_name="Diccionario")
	nexel2.to_excel(archivo,sheet_name="Nuevas_palabras")
	archivo.save()
	return(palabra_en_mensaje)
	
def diccionario_backup():
	exel=pd.read_excel(io="Diccionario.xlsx", sheet_name="Diccionario")
	exel2=pd.read_excel(io="Diccionario.xlsx", sheet_name="Nuevas_palabras")
	coldi=exel.columns[1]
	colnp=exel2.columns[1]
	listnp=[]
	listdic=[]
	palabra_en_mensaje=False
	for index, row in exel.iterrows():
		listdic.append(str(row[1]))
	for index, row in exel2.iterrows():
		listnp.append(str(row[1]))
	tiempo_cadena = time.strftime("%d-%m-%Y")#facha local dia, mes, año
	nombre="diccionario_backup_"+(str(tiempo_cadena))+".xlsx"#se le suma el formato del archivo
	archivo=pd.ExcelWriter(nombre)
	nexel=pd.DataFrame({coldi:listdic})
	nexel2=pd.DataFrame({colnp:listnp})
	nexel.to_excel(archivo,sheet_name="Diccionario")
	nexel2.to_excel(archivo,sheet_name="Nuevas_palabras")
	archivo.save()

def mcenp():#mostrar cantidad nuevas palabras
	exel=pd.read_excel(io="Diccionario.xlsx", sheet_name="Diccionario")
	exel2=pd.read_excel(io="Diccionario.xlsx", sheet_name="Nuevas_palabras")
	listnp=[]
	for index, row in exel2.iterrows():
		listnp.append(str(row[1]))
	return(int(len(listnp)))

def mp():#mostrar palabra siempre muestra la ultima
	exel=pd.read_excel(io="Diccionario.xlsx", sheet_name="Diccionario")
	exel2=pd.read_excel(io="Diccionario.xlsx", sheet_name="Nuevas_palabras")
	listnp=[]
	for index, row in exel2.iterrows():
		listnp.append(str(row[1]))
	indice_list=int(len(listnp)-1)
	return(listnp[indice_list])
def aupad():#agregar ultima palabra al diccionario
	exel=pd.read_excel(io="Diccionario.xlsx", sheet_name="Diccionario")
	exel2=pd.read_excel(io="Diccionario.xlsx", sheet_name="Nuevas_palabras")
	coldi=exel.columns[1]
	colnp=exel2.columns[1]
	listdic=[]
	listnp=[]
	for index, row in exel.iterrows():
		listdic.append(str(row[1]))
	for index, row in exel2.iterrows():
		listnp.append(str(row[1]))
	indice_list=int(len(listnp)-1)
	listdic.append(listnp[indice_list])
	listnp.pop(indice_list)
	nexel=pd.DataFrame({coldi:listdic})
	nexel2=pd.DataFrame({colnp:listnp})
	archivo=pd.ExcelWriter("Diccionario.xlsx")
	nexel.to_excel(archivo,sheet_name="Diccionario")
	nexel2.to_excel(archivo,sheet_name="Nuevas_palabras")
	archivo.save()

def dp():#denegar palabra
	exel=pd.read_excel(io="Diccionario.xlsx", sheet_name="Diccionario")
	exel2=pd.read_excel(io="Diccionario.xlsx", sheet_name="Nuevas_palabras")
	coldi=exel.columns[1]
	colnp=exel2.columns[1]
	listdic=[]
	listnp=[]
	for index, row in exel.iterrows():
		listdic.append(str(row[1]))
	for index, row in exel2.iterrows():
		listnp.append(str(row[1]))
	indice_list=int(len(listnp)-1)
	listnp.pop(indice_list)
	nexel=pd.DataFrame({coldi:listdic})
	nexel2=pd.DataFrame({colnp:listnp})
	archivo=pd.ExcelWriter("Diccionario.xlsx")
	nexel.to_excel(archivo,sheet_name="Diccionario")
	nexel2.to_excel(archivo,sheet_name="Nuevas_palabras")
	archivo.save()

def pdu():#palabra dudosa para que la revise la profe
	exel=pd.read_excel(io="Diccionario.xlsx", sheet_name="Diccionario")
	exel2=pd.read_excel(io="Diccionario.xlsx", sheet_name="Nuevas_palabras")
	exel3=pd.read_excel(io="Palabras_dudosas.xlsx")
	coldi=exel.columns[1]
	colnp=exel2.columns[1]
	colpd=exel3.columns[1]
	listnp=[]
	listdic=[]
	listpd=[]
	for index, row in exel.iterrows():
		listdic.append(str(row[1]))
	for index, row in exel2.iterrows():
		listnp.append(str(row[1]))
	for index, row in exel3.iterrows():
		listpd.append(str(row[1]))
	indice_list=int(len(listnp)-1)
	listpd.append(listnp[indice_list])
	listnp.pop(indice_list)
	nexel=pd.DataFrame({coldi:listdic})
	nexel2=pd.DataFrame({colnp:listnp})
	nexel3=pd.DataFrame({colpd:listpd})
	archivo=pd.ExcelWriter("Diccionario.xlsx")
	nexel.to_excel(archivo,sheet_name="Diccionario")
	nexel2.to_excel(archivo,sheet_name="Nuevas_palabras")
	archivo.save()
	archivo2=pd.ExcelWriter("Palabras_dudosas.xlsx")
	nexel3.to_excel(archivo2)
	archivo2.save()

def palabras_comandos():
	exel=pd.read_excel("comandos.xlsx")
	listpc=[]
	for index, row in exel.iterrows():
		listpc.append(str(row[1]))
	return(listpc)

def palabras_denegadas(palabra):
	palabra_denegada=False
	exel=pd.read_excel("Palabras_denegadas.xlsx")
	listpade=[]
	for index, row in exel.iterrows():
		listpade.append(str(row[1]))
	for i in range(0,len(listpade)):
		if str(palabra) == str(listpade[i]):
			palabra_denegada=True
	return(palabra_denegada)


def mostrar_diccionario():
	exel=pd.read_excel("Diccionario.xlsx",sheet_name="Diccionario")
	return(exel)

def mostrar_nuevasp():
	exel=pd.read_excel("Diccionario.xlsx",sheet_name="Diccionario")
	exel2=pd.read_excel("Diccionario.xlsx",sheet_name="Nuevas_palabras")
	return(exel2)
def mostrar_palabrasdu():
	exel=pd.read_excel("Palabras_dudosas.xlsx")
	return(exel)
def mostrar_palabrasde():
	exel=pd.read_excel("Palabras_denegadas.xlsx")
	return(exel)

def mostrar_comandos():
	exel=pd.read_excel("comandos.xlsx")
	colc=exel.columns[1]
	listc=[]
	for index,row in exel.iterrows():
		listc.append(str(row[1]))
	return(listc)
def mostrar_svacio():
	exel=pd.read_excel(io="Palabras_dudosas.xlsx")
	listpd=[]
	vacio=False
	for index, row in exel.iterrows():
		listpd.append(str(row[1]))
	if len(listpd)==0:
		vacio=True
	return(vacio)
def mostrar_upalabrad():
	exel=pd.read_excel(io="Palabras_dudosas.xlsx")
	listpd=[]
	for index, row in exel.iterrows():
		listpd.append(str(row[1]))
	indice_list=int(len(listpd)-1)
	return(listpd[indice_list])
#hola
def agregar_palabrasddi():#agregar palabra dudasa al diccionario
	exel=pd.read_excel(io="Diccionario.xlsx", sheet_name="Diccionario")
	exel2=pd.read_excel(io="Diccionario.xlsx", sheet_name="Nuevas_palabras")
	exel3=pd.read_excel(io="Palabras_dudosas.xlsx")
	coldi=exel.columns[1]
	colnp=exel2.columns[1]
	colpd=exel3.columns[1]
	listdic=[]
	listnp=[]
	listpd=[]
	for index,row in exel.iterrows():
		listdic.append(str(row[1]))
	for index,row in exel2.iterrows():
		listnp.append(str(row[1]))
	for index,row in exel3.iterrows():
		listpd.append(str(row[1]))
	indice_list=int(len(listpd)-1)
	listdic.append(listpd[indice_list])
	listpd.pop(indice_list)
	nexel=pd.DataFrame({coldi:listdic})
	nexel2=pd.DataFrame({colnp:listnp})
	nexel3=pd.DataFrame({colpd:listpd})
	archivo=pd.ExcelWriter("Diccionario.xlsx")
	archivo2=pd.ExcelWriter("Palabras_dudosas.xlsx")
	nexel.to_excel(archivo,sheet_name="Diccionario")
	nexel2.to_excel(archivo,sheet_name="Nuevas_palabras")
	nexel3.to_excel(archivo2)
	archivo.save()
	archivo2.save()

def denegar_palabrad():#denegar palabra dudosa
	exel=pd.read_excel("Palabras_dudosas.xlsx")
	exel2=pd.read_excel("Palabras_denegadas.xlsx")
	colpdu=exel.columns[1]
	colpde=exel2.columns[1]
	listpdu=[]
	listpde=[]
	for index,row in exel.iterrows():
		listpdu.append(str(row[1]))
	for index,row in exel2.iterrows():
		listpde.append(str(row[1]))
	indice_list=int(len(listpdu)-1)
	listpde.append(listpdu[indice_list])
	listpdu.pop(indice_list)
	nexel=pd.DataFrame({colpdu:listpdu})
	nexel2=pd.DataFrame({colpde:listpde})
	archivo=pd.ExcelWriter("Palabras_dudosas.xlsx")
	archivo2=pd.ExcelWriter("Palabras_denegadas.xlsx")
	nexel.to_excel(archivo)
	nexel2.to_excel(archivo2)
	archivo.save()
	archivo2.save()