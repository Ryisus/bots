import pandas as pd

def nuevo_tablero():
	tablero=[[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
	archivo=pd.ExcelWriter("tablero.xlsx")
	ta1=tablero[0]
	ta2=tablero[1]
	ta3=tablero[2]
	nexel=pd.DataFrame({0:ta1,1:ta2,2:ta3})
	nexel.to_excel(archivo)
	archivo.save()
	my_file=open("turno.txt","w")
	my_file.write(str(0))
	my_file.close()
	my_file=open("contador.txt","w")
	my_file.write(str(0))
	my_file.close()
	my_file=open("ganador.txt","w")
	my_file.write(str(0))
	my_file.close()
	my_file=open("jugador1.txt", "w")
	my_file.write(str(0))
	my_file.close()
	my_file=open("jugador2.txt", "w")
	my_file.write(str(0))
	my_file.close()
	my_file=open("jugadores.txt","w")
	my_file.write(str(0))
	my_file.close()

def armar_tablero():
	tablero=[[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
	exel=pd.read_excel("tablero.xlsx",usecols=[1,2,3])
	list0=list(exel[0])
	list1=list(exel[1])
	list2=list(exel[2])
	for i in range(0,3):
		tablero[i][0]=list0[i]
		tablero[i][1]=list1[i]
		tablero[i][2]=list2[i]
	return(tablero)



def modificar_tablero(tablero):
	archivo=pd.ExcelWriter("tablero.xlsx")
	t0=tablero[0]
	t1=tablero[1]
	t2=tablero[2]
	ta1=["","",""]
	ta2=["","",""]
	ta3=["","",""]
	ta1[0]=t0[0]
	ta2[0]=t0[1]
	ta3[0]=t0[2]
	ta1[1]=t1[0]
	ta2[1]=t1[1]
	ta3[1]=t1[2]
	ta1[2]=t2[0]
	ta2[2]=t2[1]
	ta3[2]=t2[2]
	nexel=pd.DataFrame({0:ta1,1:ta2,2:ta3})
	nexel.to_excel(archivo)
	archivo.save()

def jugador_1(id):
	my_file=open("jugador1.txt","w")
	my_file.write(str(id))
	my_file.close()
	turno=r_turno()
	if turno==0:
		c_turno(1)

def jugador_2(id):
	my_file=open("jugador2.txt","w")
	my_file.write(str(id))
	my_file.close()
	turno=r_turno()
	if turno==0:
		c_turno(2)

def c_turno(tj):
	my_file=open("turno.txt","w")
	my_file.write(str(tj))
	my_file.close()
def r_turno():
	my_file=open("turno.txt","r")
	turno=int(my_file.read())
	my_file.close()
	return(turno)
def cero_cero(id):
	tablero=armar_tablero()
	my_file=open("jugador1.txt","r")
	jugador1=int(my_file.read())
	my_file.close()
	my_file=open("jugador2.txt","r")
	jugador2=int(my_file.read())
	my_file.close()
	turno=r_turno()
	if id==jugador1 and turno==1 and tablero[0][0]!='x' and tablero[0][0]!='o' :
		tablero[0][0]='o'
		modificar_tablero(tablero)
		c_turno(2)
		aumentar_contador()

	else:
		if id==jugador2 and turno==2 and tablero[0][0]!='o' and tablero[0][0]!='x':
			tablero[0][0]='x'
			modificar_tablero(tablero)
			c_turno(1)
			aumentar_contador()

def cero_uno(id):
	tablero=armar_tablero()
	my_file=open("jugador1.txt","r")
	jugador1=int(my_file.read())
	my_file.close()
	my_file=open("jugador2.txt","r")
	jugador2=int(my_file.read())
	my_file.close()
	turno=r_turno()
	if id==jugador1 and turno==1 and tablero[0][1]!='x' and tablero[0][1]!='o' :
		tablero[0][1]='o'
		modificar_tablero(tablero)
		c_turno(2)
		aumentar_contador()
	else:
		if id==jugador2 and turno==2 and tablero[0][1]!='o' and tablero[0][1]!='x':
			tablero[0][1]='x'
			modificar_tablero(tablero)
			c_turno(1)
			aumentar_contador()

def cero_dos(id):
	tablero=armar_tablero()
	my_file=open("jugador1.txt","r")
	jugador1=int(my_file.read())
	my_file.close()
	my_file=open("jugador2.txt","r")
	jugador2=int(my_file.read())
	my_file.close()
	turno=r_turno()
	if id==jugador1 and turno==1 and tablero[0][2]!='x' and tablero[0][2]!='o' :
		tablero[0][2]='o'
		print(f"\n\n{tablero}\n\n")
		modificar_tablero(tablero)
		c_turno(2)
		aumentar_contador()
	else:
		if id==jugador2 and turno==2 and tablero[0][2]!='o' and tablero[0][2]!='x':
			tablero[0][2]='x'
			modificar_tablero(tablero)
			c_turno(1)
			aumentar_contador()

def uno_cero(id):
	tablero=armar_tablero()
	my_file=open("jugador1.txt","r")
	jugador1=int(my_file.read())
	my_file.close()
	my_file=open("jugador2.txt","r")
	jugador2=int(my_file.read())
	my_file.close()
	turno=r_turno()
	if id==jugador1 and turno==1 and tablero[1][0]!='x' and tablero[1][0]!='o' :
		tablero[1][0]='o'
		modificar_tablero(tablero)
		c_turno(2)
		aumentar_contador()
	else:
		if id==jugador2 and turno==2 and tablero[1][0]!='o' and tablero[1][0]!='x':
			tablero[1][0]='x'
			modificar_tablero(tablero)
			c_turno(1)
			aumentar_contador()

def uno_uno(id):
	tablero=armar_tablero()
	my_file=open("jugador1.txt","r")
	jugador1=int(my_file.read())
	my_file.close()
	my_file=open("jugador2.txt","r")
	jugador2=int(my_file.read())
	my_file.close()
	turno=r_turno()
	if id==jugador1 and turno==1 and tablero[1][1]!='x' and tablero[1][1]!='o' :
		tablero[1][1]='o'
		modificar_tablero(tablero)
		c_turno(2)
		aumentar_contador()
	else:
		if id==jugador2 and turno==2 and tablero[1][1]!='o' and tablero[1][1]!='x':
			tablero[1][1]='x'
			modificar_tablero(tablero)
			c_turno(1)
			aumentar_contador()

def uno_dos(id):
	tablero=armar_tablero()
	my_file=open("jugador1.txt","r")
	jugador1=int(my_file.read())
	my_file.close()
	my_file=open("jugador2.txt","r")
	jugador2=int(my_file.read())
	my_file.close()
	turno=r_turno()
	if id==jugador1 and turno==1 and tablero[1][2]!='x' and tablero[1][2]!='o' :
		tablero[1][2]='o'
		modificar_tablero(tablero)
		c_turno(2)
		aumentar_contador()
	else:
		if id==jugador2 and turno==2 and tablero[1][2]!='o' and tablero[1][2]!='x':
			tablero[1][2]='x'
			modificar_tablero(tablero)
			c_turno(1)
			aumentar_contador()

def dos_cero(id):
	tablero=armar_tablero()
	my_file=open("jugador1.txt","r")
	jugador1=int(my_file.read())
	my_file.close()
	my_file=open("jugador2.txt","r")
	jugador2=int(my_file.read())
	my_file.close()
	turno=r_turno()
	if id==jugador1 and turno==1 and tablero[2][0]!='x' and tablero[2][0]!='o' :
		tablero[2][0]='o'
		modificar_tablero(tablero)
		c_turno(2)
		aumentar_contador()
	else:
		if id==jugador2 and turno==2 and tablero[2][0]!='o' and tablero[2][0]!='x':
			tablero[2][0]='x'
			modificar_tablero(tablero)
			c_turno(1)
			aumentar_contador()
def dos_uno(id):
	tablero=armar_tablero()
	my_file=open("jugador1.txt","r")
	jugador1=int(my_file.read())
	my_file.close()
	my_file=open("jugador2.txt","r")
	jugador2=int(my_file.read())
	my_file.close()
	turno=r_turno()
	if id==jugador1 and turno==1 and tablero[2][1]!='x' and tablero[2][1]!='o' :
		tablero[2][1]='o'
		modificar_tablero(tablero)
		c_turno(2)
		aumentar_contador()
	else:
		if id==jugador2 and turno==2 and tablero[2][1]!='o' and tablero[2][1]!='x':
			tablero[2][1]='x'
			modificar_tablero(tablero)
			c_turno(1)
			aumentar_contador()
def dos_dos(id):
	tablero=armar_tablero()
	my_file=open("jugador1.txt","r")
	jugador1=int(my_file.read())
	my_file.close()
	my_file=open("jugador2.txt","r")
	jugador2=int(my_file.read())
	my_file.close()
	turno=r_turno()

	if id==jugador1 and turno==1 and tablero[2][2]!='x' and tablero[2][2]!='o' :
		tablero[2][2]='o'
		modificar_tablero(tablero)
		c_turno(2)
		aumentar_contador()
	else:
		if id==jugador2 and turno==2 and tablero[2][2]!='o' and tablero[2][2]!='x':
			tablero[2][2]='x'
			modificar_tablero(tablero)
			c_turno(1)
			aumentar_contador()
def aumentar_contador():
	my_file=open("contador.txt","r")
	contador=int(my_file.read())
	my_file.close()
	my_file=open("contador.txt","w")
	contador=contador+1
	my_file.write(str(contador))
	my_file.close()
def final_contador():
	my_file=open("contador.txt","w")
	contador=9
	my_file.write(str(contador))
	my_file.close()

def r_contador():
	my_file=open("contador.txt","r")
	contador=int(my_file.read())
	return(contador)

def revisar_ganador():
	tablero=armar_tablero()
	contador=r_contador()
	my_file=open("ganador.txt","r")
	ganador=int(my_file.read())
	my_file.close()
	if ganador==0:
		if contador >= 3:
			if tablero[0][0]==tablero[1][1] and tablero[1][1]==tablero[2][2]:
				if tablero[0][0]=='o':
					my_file=open("ganador.txt","w")
					ganador=1
					my_file.write(str(ganador))
					my_file.close()
					final_contador()
				else:
					if tablero[0][0]=='x':
						my_file=open("ganador.txt","w")
						ganador=2
						my_file.write(str(ganador))
						my_file.close()
						final_contador()
			if tablero[0][2]==tablero[1][1] and tablero[1][1]==tablero[2][0]:
				if tablero[0][2]=='o':
					my_file=open("ganador.txt","w")
					ganador=1
					my_file.write(str(ganador))
					my_file.close()
					final_contador()
				else:
					if tablero[0][2]=='x':
						my_file=open("ganador.txt","w")
						ganador=2
						my_file.write(str(ganador))
						my_file.close()
						final_contador()
			for i in range(0,3):
				if tablero[i][0]==tablero[i][1]and tablero[i][1]==tablero[i][2]:
					if tablero[i][0]=='o':
						my_file=open("ganador.txt","w")
						ganador=1
						my_file.write(str(ganador))
						my_file.close()
						final_contador()
					else:
						if tablero[i][0]=='x':
							my_file=open("ganador.txt","w")
							ganador=2
							my_file.write(str(ganador))
							my_file.close()
							final_contador()
			for i in  range(0,3):
				if tablero[0][i]==tablero[1][i] and tablero[1][i]==tablero[2][i]:
					if tablero[0][i]=='o':
						my_file=open("ganador.txt","w")
						ganador=1
						my_file.write(str(ganador))
						my_file.close()
						final_contador()
					else:
						if tablero[0][i]=='x':
							my_file=open("ganador.txt","w")
							ganador=2
							my_file.write(str(ganador))
							my_file.close()
							final_contador()
def mostrar_ganador():
	my_file=open("ganador.txt","r")
	ganador=int(my_file.read())
	my_file.close()
	return(ganador)

def sumar_jugadores():
	my_file=open("jugadores.txt","r")
	jugadores=int(my_file.read())
	my_file.close()
	if jugadores == 0 or jugadores==1:
		jugadores=jugadores+1
		my_file=open("jugadores.txt", "w")
		my_file.write(str(jugadores))
		my_file.close()