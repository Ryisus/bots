import os, discord, sys, random, time, logging
from turtle import title
from discord.ext import commands

def guardarenarchivo(idauthor):
	idestidiantes.append(idauthor)
	idestudiantes=[848254286437023805,"\n",367082134927573013,"\n",900501480946139167] # test
	archivoids=open("idestudiantes.txt","w")
	archivoids.write(str(idestudiantes))
	archivoids.close()
	print("se logeo su id")
	idestidiantes=[0]
	listalinea=list()
	archivoids=open("idestidiantes.txt","r")
	listalinea=archivoids.readlines()
	lineastring=str
	letra=str
	for letra in listalinea:
		lineastring=lineastring+letra
	print(lineastring)
	#idestudiantes=int(lineastring)
	#print(idestidiantes)