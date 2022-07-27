import os, discord, sys, random, time, logging
from turtle import title
from discord.ext import commands
from pruebas2 import guardarenarchivo
import modificar_exel
import diccionario
import ter
# import off

# registros con el modulo logger de discord.py

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# intentos

intents = discord.Intents.default()
intents.members = True

# info

prefix = "!"
bot = commands.Bot(command_prefix=prefix)

# inicio

@bot.event
async def on_ready():
        print('\nBot iniciado!') # mira el comentario abajo >
        await bot.change_presence (activity=discord.Activity(type=discord.ActivityType.watching,name=' HolaSoyGerman ')) # Esto es para poner el estado del bot

async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Bienvenido {0.mention} a {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
            # esto lo saque de la guia de discord.py

# comandos


def restart_bot(): #para reiniciar bot linea 51
  os.execv(sys.executable, ['python'] + sys.argv)#metodo para reiniciar el bot

@bot.command(name ="reiniciar")
async def reiniciar(ctx):
    id = int(ctx.author.id)#guarda la id del que escribio el mensaje
    if id == 848254286437023805 or id==367082134927573013 or id==900501480946139167: # IDS: Bauti pr Jesus # solo estas id tienen permiso para reiniciar el bot
        await ctx.send("Reiniciando el bot...")#el bot manda el mensaje si tenemos los permisos
        restart_bot()#se llama el metodo
    else:
        await ctx.send("No tienes los permisos suficientes!")#manda este mensaje si no tenemos permiso

@bot.command(name ="restart")
async def reiniciar2(ctx):#otro reiniciar, pero este es por la id de un rol
    id = int(ctx.Role.id)#saca la id del rol del que haya enviado el mensaje
    if id == 897631749356552242 : # IDS: Bauti pr Jesus
        await ctx.send("Reiniciando el bot...")#el bot manda el mensaje si tenemos los permisos
        restart_bot()#se llama el metodo
    else:
        await ctx.send("No tienes los permisos suficientes!")#manda este mensaje si no tenemos permiso

@bot.command(name= 'ping')
async def ping(ctx):
    antes = time.monotonic()
    m=await ctx.send('Pong!')
    p1=(time.monotonic()-antes)*1000 #variable de tiempo
    p2=(str(p1).split('.'))[0]#para escribir nomas
    await m.edit(content=f'Pong! (ms={p2})')

@bot.command(name= 'sex')
async def sex(ctx):
    await ctx.message.add_reaction(emoji="🍆")#simple mente agrega una reaccion
    await ctx.message.add_reaction(emoji="🍑")#simple mente agrega una reaccion

@bot.command(name="sexo")
async def sexo(ctx):
    message= "**SEXOO**"
    react_messasge = await ctx.send(message)#escribe el mensaje sexo y reacciona lo siguiente
    await react_messasge.add_reaction(emoji="🍆")#añada reaccion
    await react_messasge.add_reaction(emoji="🍑")#añade reaccion

@bot.command(name="backup")
async def backup(ctx):
    id=int(ctx.author.id)#mira si el que escribio el comando tiene permisos
    if id == 848254286437023805 or id==367082134927573013 or id==900501480946139167: # IDS: Bauti pr Jesus
        msg=await ctx.send("Cargando...")#manda un mensaje
        modificar_exel.backup()#llama al metodo backup del archivo modificar_exel
        diccionario.diccionario_backup()#llama al metodo del archivo diccionario
        await msg.edit(content="Se realizo el BackUp")#edita el contenido del mensaje
    else:
        await ctx.send("No tienes los permisos suficientes!")#manda un mensaje

@bot.command(name="register")
async def registro(ctx):
    canalID= int (ctx.channel.id)#mira la id del canal donde se envio el comando

    print(canalID)
    if ctx.channel.id == 897596660002218016: # Canal de los pibes
        my_file=open("idestudiantes.txt","r")#abre un archivo txt en modo lectura
        content = my_file.read()#guarda todo lo del archivo dentro de una variable
        content_list = content.split(', ')#devide el contenido de la variable donde se encuentren ", " y lo guarda en una lista
        removetable = str.maketrans('', '', '[]')#esto para borrar las llaves, ya que por la lectura del archivo se quedan
        out_list = [s.translate(removetable) for s in content_list]#lo guardamos en otra lista ya con los datos procesados
        out_list[0]="0"#en el subindice 0 se modifica el valor ya que sino rompe el archivo
        my_file.close()#cerramos el archivo
        
        
        idautor=int(ctx.author.id)#mira la id del autr que envio el comando

        msg=await ctx.send("Cargando...")#manda un mensaje

        estaenlista=False#esta variable funciona como interruptor para ver si esta en la lista de id de estudiantes o no
        for i in range(0,len(out_list)):#recorre de principio a fin la lista con las ids
            out_list[i]=int(out_list[i])#transforma las id de str a int
            if str(idautor)==str(out_list[i]):#las conmparamos en str por las dudas
                estaenlista=True#se pone en true si encuentra la id en la lista

        if estaenlista==True:
            await msg.edit(content="Su ID ya se encuentra registrada!")#modifica el mensaje en caso de que la id ya estuviera registrada
        else:
            if estaenlista==False:#en caso contrario
                out_list.append(idautor)#agrega la id nueva al final del vvector donde guardo las id
                my_file=open("idestudiantes.txt","w")#abro el archivo txt en modo escritura
                out_list[0]="0"#modifico el primer subindice para no romper el archivo
                my_file.write(str(out_list))#en los archivos txt solo se pueden escribir valosres str, por eso convierto la lista de enteeros en int
                my_file.close()#cierro el archivo
                usdi=await bot.fetch_user(idautor)#se guanda el nombre de usuario y su discriminator junto
                modificar_exel.agregar_usuario(idautor,usdi.name,0,usdi.discriminator," ")#parametros id,nombre usuario,puntos,discriminator y mensaje
                await msg.edit(content="Listo! estas Registrado")#modifico el mensaje
                
    elif ctx.channel.id == 983398887274455040:#Comparacion canal colegio
        my_file=open("idestudiantes.txt","r")#abre un archivo txt en modo lectura
        content = my_file.read()#guarda todo lo del archivo dentro de una variable
        content_list = content.split(', ')#devide el contenido de la variable donde se encuentren ", " y lo guarda en una lista
        removetable = str.maketrans('', '', '[]')#esto para borrar las llaves, ya que por la lectura del archivo se quedan
        out_list = [s.translate(removetable) for s in content_list]#lo guardamos en otra lista ya con los datos procesados
        out_list[0]="0"#en el subindice 0 se modifica el valor ya que sino rompe el archivo
        my_file.close()#cerramos el archivo
        

        idautor=int(ctx.author.id)#mira la id del autr que envio el comando

        msg=await ctx.send("Cargando...")#manda un mensaje

        estaenlista=False#esta variable funciona como interruptor para ver si esta en la lista de id de estudiantes o no
          
        for i in range(0,len(out_list)):#recorre de principio a fin la lista con las ids
            out_list[i]=int(out_list[i])#transforma las id de str a int
            if str(idautor)==str(out_list[i]):#las conmparamos en str por las dudas
                estaenlista=True#se pone en true si encuentra la id en la lista

        if estaenlista==True:
            await msg.edit(content="Su ID ya se encuentra registrada!")#modifica el mensaje en caso de que la id ya estuviera registrada
        else:
            if estaenlista==False:#en caso contrario
                out_list.append(idautor)#agrega la id nueva al final del vvector donde guardo las id
                my_file=open("idestudiantes.txt","w")#abro el archivo txt en modo escritura
                out_list[0]="0"#modifico el primer subindice para no romper el archivo
                my_file.write(str(out_list))#en los archivos txt solo se pueden escribir valosres str, por eso convierto la lista de enteeros en int
                my_file.close()#cierro el archivo
                usdi=await bot.fetch_user(idautor)#se guanda el nombre de usuario y su discriminator junto
                modificar_exel.agregar_usuario(idautor,usdi.name,0,usdi.discriminator," ")#parametros id,nombre usuario,puntos,discriminator y mensaje
                await msg.edit(content="Listo! estas Registrado")#modifico el mensaje
@bot.command(name="ad")#actualizar diccionario
async def actualizar_interruptor_diccionario(ctx):
    canalID= int (ctx.channel.id)#guarda la id del canal de donde se envio el comando
    idcanal=int(991003514010472548)# id ya establesida del canal filtrado palabra espanglishde comando del bot 
    if canalID == idcanal:#verifica si es el canal adecuado
        numpa=diccionario.mcenp()#llamo un metodo que me devuelve un int con la cantidad de palabras que hay para filtrar
        msg=await ctx.send(str(f"Hay {numpa} palabras posibles"))#muestro el mensajo
        pm=diccionario.mp()#llamo el metodo que me retorna la ultima palabra de una lista de Nuevas_palabras
        await ctx.send(f"La palabra a filtrar es:{pm}")#muestro la ultima palabra
        await ctx.send("!1-Aceptar en diccionario\n!2-Denegar en diccionario\n!3-Palabra dudosa\n!4-Mostrar otra palabra\n!5-Salir")#mustro los comandos de control
        my_file=open("interruptor.txt","w")#abro un archivo y lo uso como intteruptor ya que las variables globales no funcionan para el proposito que yo quiero
        my_file.write(str(1))#le cambio el valor a 1 = encendido #el valor predeterminado con el que empieza el archivo es 0 = apagado
@bot.command(name="1")#actualizar diccionario
async def agregar_palabra_diccionario(ctx):
    canalID= int (ctx.channel.id)#guarda la id del canal de donde se envio el comando
    idcanal=int(991003514010472548)# id ya establesida del canal filtrado palabra espanglishde comando del bot 
    if(canalID==idcanal):#verifica si es el canal adecuado
        my_file=open("interruptor.txt","r")#abre el archivo interreptor en modo lectura
        interruptor=int(my_file.read())#lo lee como un int
        if(interruptor==1):#verifica si el interruptor esta prendido para que los comandos funcionen
            msg=await ctx.send("Cargando...")#manda el mensaje cargando
            diccionario.aupad()#llama el metodo que agrega la ultima palabra de Nuevas_palabras a Diccionario
            await msg.edit(content="Se agrego al diccionario")#modifica el contenido del mensaje
@bot.command(name="2")#actualizar diccionario
async def denegar_palabra(ctx):
    canalID= int (ctx.channel.id)#guarda la id del canal de donde se envio el comando
    idcanal=int(991003514010472548)# id ya establesida del canal filtrado palabra espanglishde comando del bot 
    if(canalID==idcanal):#verifica si es el canal adecuado
        my_file=open("interruptor.txt","r")#abre el archivo interreptor en modo lectura
        interruptor=int(my_file.read())#lo lee como un int
        if(interruptor==1):#verifica si el interruptor esta prendido para que los comandos funcionen
            msg=await ctx.send("Cargando...")#manda un mensaje
            diccionario.dp()#llama al metodo denegar palabra de diccionario
            await msg.edit(content="Se denego la palabra")#modifica el contenido del mensaje
@bot.command(name="3")#actualizar diccionario
async def palabra_dudosa(ctx):
    canalID= int (ctx.channel.id)#guarda la id del canal de donde se envio el comando
    idcanal=int(991003514010472548)# id ya establesida del canal filtrado palabra espanglishde comando del bot 
    if(canalID==idcanal):#verifica si es el canal adecuado
        my_file=open("interruptor.txt","r")#abre el archivo interreptor en modo lectura
        interruptor=int(my_file.read())#lo lee como un int
        if(interruptor==1):#verifica si el interruptor esta prendido para que los comandos funcionen
            msg=await ctx.send("Cargando...")#manda un mensaje
            diccionario.pdu()#llama al metodo palabra dudosa de diccionario
            await msg.edit(content="Se agrego a palabras dudosas")#modifica el contenido del mensaje
@bot.command(name="4")#actualizar diccionario
async def mostrar_palabra(ctx):
    canalID= int (ctx.channel.id)#guarda la id del canal de donde se envio el comando
    idcanal=int(991003514010472548)# id ya establesida del canal filtrado palabra espanglishde comando del bot 
    if(canalID==idcanal):#verifica si es el canal adecuado
        my_file=open("interruptor.txt","r")#abre el archivo interreptor en modo lectura
        interruptor=int(my_file.read())#lo lee como un int
        if(interruptor==1):#verifica si el interruptor esta prendido para que los comandos funcionen
            msg=await ctx.send("Cargando...")#manda un mensaje
            pm=diccionario.mp()#llama al metodo mostrar palabra de diccionario, retorna la ultima palabra
            await msg.edit(content=f"La palabra es:{pm}")#edita el contenido del mensaje
@bot.command(name="5")#actualizar interruptor
async def apagar_interruptor(ctx):
    canalID= int (ctx.channel.id)#guarda la id del canal de donde se envio el comando
    idcanal=int(991003514010472548)# id ya establesida del canal filtrado palabra espanglishde comando del bot 
    if(canalID==idcanal):#verifica si es el canal adecuado
        my_file=open("interruptor.txt","r")#abre el archivo interreptor en modo lectura
        interruptor=int(my_file.read())#lo lee como un int
        if(interruptor==1):#verifica si el interruptor esta prendido para que los comandos funcionen
            msg=await ctx.send("Cargando...")#mandda un mensaje
            my_file=open("interruptor.txt","w")#abre el archivo interruptor
            my_file.write(str(0))#escribe en el archivo
            my_file.close()#lo cierra
            await msg.edit(content="Se salio del filtrado de palabras")#edita el contenido del mensaje

#comandos tres en  raya
@bot.command(name="jugar")
async def iniciar_ter(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID:
        ter.nuevo_tablero()
        my_file=open("terinterruptor.txt", "w")
        my_file.write(str(1))
        my_file.close()
        await ctx.send("Elegir jugador que empieza\n !j1 = 'o'\n !j2 = 'x' \n !t para mostrar el tablero")
@bot.command(name="j1")
async def iniciar_ter(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    my_file=open("jugador1.txt","r")
    idjugador1=int(my_file.read())
    if idcanalter==canalID and inter == 1 :
        if idjugador1==0:
            idjugador=int(ctx.author.id)
            ter.jugador_1(idjugador)
            ter.sumar_jugadores()
            usdi=await bot.fetch_user(idjugador)
            await ctx.send(f"{usdi.name} ahora es Jugador 1")
        else:
            await ctx.send("Jugador 1 ya ha sido elegido, elige otro jugador")

@bot.command(name="j2")
async def iniciar_ter(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    my_file=open("jugador2.txt","r")
    idjugador2=int(my_file.read())
    if idcanalter==canalID and inter == 1 :
        if idjugador2==0:
            idjugador=int(ctx.author.id)
            ter.jugador_2(idjugador)
            ter.sumar_jugadores()
            usdi=await bot.fetch_user(idjugador)
            await ctx.send(f"{usdi.name} ahora es Jugador 2")
        else:
            await ctx.send("Jugador 2 ya ha sido elegido, elige otro jugador")

@bot.command(name="t")
async def mostrar_tablero(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        tablero=ter.armar_tablero()
        await ctx.send(f"| {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |\n| {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |\n| {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")
        turno=ter.r_turno()
        await ctx.send(f"Es turno del jugador {turno}")

@bot.command(name="00")
async def t00(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        idautor=int(ctx.author.id)
        ter.cero_cero(idautor)
        tablero=ter.armar_tablero()
        await ctx.send(f"| {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |\n| {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |\n| {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")

        ter.revisar_ganador()
        ganador=ter.mostrar_ganador()
        if ganador!=0:
            await ctx.send(f"Gano el jugador {ganador}")
            my_file=open("terinterruptor.txt","w")
            my_file.write(str(0))
            my_file.close()
        else:
            turno=ter.r_turno()
            await ctx.send(f"Es turno del jugador {turno}")
@bot.command(name="01")
async def t01(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        idautor=int(ctx.author.id)
        ter.cero_uno(idautor)
        tablero=ter.armar_tablero()
        await ctx.send(f"| {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |\n| {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |\n| {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")

        ter.revisar_ganador()
        ganador=ter.mostrar_ganador()
        if ganador!=0:
            await ctx.send(f"Gano el jugador {ganador}")
            my_file=open("terinterruptor.txt","w")
            my_file.write(str(0))
            my_file.close()
        else:
            turno=ter.r_turno()
            await ctx.send(f"Es turno del jugador {turno}")
@bot.command(name="02")
async def t02(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        idautor=int(ctx.author.id)
        ter.cero_dos(idautor)
        tablero=ter.armar_tablero()
        await ctx.send(f"| {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |\n| {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |\n| {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")

        ter.revisar_ganador()
        ganador=ter.mostrar_ganador()
        if ganador!=0:
            await ctx.send(f"Gano el jugador {ganador}")
            my_file=open("terinterruptor.txt","w")
            my_file.write(str(0))
            my_file.close()
        else:
            turno=ter.r_turno()
            await ctx.send(f"Es turno del jugador {turno}")
@bot.command(name="10")
async def t10(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        idautor=int(ctx.author.id)
        ter.uno_cero(idautor)
        tablero=ter.armar_tablero()
        await ctx.send(f"| {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |\n| {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |\n| {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")

        ter.revisar_ganador()
        ganador=ter.mostrar_ganador()
        if ganador!=0:
            await ctx.send(f"Gano el jugador {ganador}")
            my_file=open("terinterruptor.txt","w")
            my_file.write(str(0))
            my_file.close()
        else:
            turno=ter.r_turno()
            await ctx.send(f"Es turno del jugador {turno}")
@bot.command(name="11")
async def t11(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        idautor=int(ctx.author.id)
        ter.uno_uno(idautor)
        tablero=ter.armar_tablero()
        await ctx.send(f"| {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |\n| {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |\n| {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")

        ter.revisar_ganador()
        ganador=ter.mostrar_ganador()
        if ganador!=0:
            await ctx.send(f"Gano el jugador {ganador}")
            my_file=open("terinterruptor.txt","w")
            my_file.write(str(0))
            my_file.close()
        else:
            turno=ter.r_turno()
            await ctx.send(f"Es turno del jugador {turno}")
@bot.command(name="12")
async def t12(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        idautor=int(ctx.author.id)
        ter.uno_dos(idautor)
        tablero=ter.armar_tablero()
        await ctx.send(f"| {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |\n| {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |\n| {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")

        ter.revisar_ganador()
        ganador=ter.mostrar_ganador()
        if ganador!=0:
            await ctx.send(f"Gano el jugador {ganador}")
            my_file=open("terinterruptor.txt","w")
            my_file.write(str(0))
            my_file.close()
        else:
            turno=ter.r_turno()
            await ctx.send(f"Es turno del jugador {turno}")
@bot.command(name="20")
async def t20(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        idautor=int(ctx.author.id)
        ter.dos_cero(idautor)
        tablero=ter.armar_tablero()
        await ctx.send(f"| {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |\n| {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |\n| {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")

        ter.revisar_ganador()
        ganador=ter.mostrar_ganador()
        if ganador!=0:
            await ctx.send(f"Gano el jugador {ganador}")
            my_file=open("terinterruptor.txt","w")
            my_file.write(str(0))
            my_file.close()
        else:
            turno=ter.r_turno()
            await ctx.send(f"Es turno del jugador {turno}")
@bot.command(name="21")
async def t21(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        idautor=int(ctx.author.id)
        ter.dos_uno(idautor)
        tablero=ter.armar_tablero()
        await ctx.send(f"| {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |\n| {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |\n| {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")

        ter.revisar_ganador()
        ganador=ter.mostrar_ganador()
        if ganador!=0:
            await ctx.send(f"Gano el jugador {ganador}")
            my_file=open("terinterruptor.txt","w")
            my_file.write(str(0))
            my_file.close()
        else:
            turno=ter.r_turno()
            await ctx.send(f"Es turno del jugador {turno}")
@bot.command(name="22")
async def t22(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        idautor=int(ctx.author.id)
        ter.dos_dos(idautor)
        tablero=ter.armar_tablero()
        await ctx.send(f"| {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} |\n| {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} |\n| {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} |")

        ter.revisar_ganador()
        ganador=ter.mostrar_ganador()
        if ganador!=0:
            await ctx.send(f"Gano el jugador {ganador}")
            my_file=open("terinterruptor.txt","w")
            my_file.write(str(0))
            my_file.close()
        else:
            turno=ter.r_turno()
            await ctx.send(f"Es turno del jugador {turno}")
@bot.command(name="salir")
async def terminar_ter(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=992022684345049179#ID espanglish tres-en-raya
    my_file=open("terinterruptor.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        my_file=open("terinterruptor.txt", "w")
        my_file.write(str(0))
        my_file.close()
        await ctx.send("Dejaste de jugar")
@bot.command(name="pdudosa")
async def interruptor_pdu(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=991003514010472548#ID espanglish filtrado palabras
    my_file=open("interruptorpdu.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 0:
        vacio=diccionario.mostrar_svacio()
        if vacio == False:
            pm=diccionario.mostrar_upalabrad()#llamo el metodo que me retorna la ultima palabra de una lista de Palabras dudosas
            await ctx.send(f"La palabra dudosa a filtrar es:{pm}")#muestro la ultima palabra
            await ctx.send("!6-Aceptar en diccionario\n!7-Denegar \n!8-Mostrar otra palabra\n!9-Salir")#mustro los comandos de control
            my_file=open("interruptorpdu.txt","w")#abro un archivo y lo uso como intteruptor ya que las variables globales no funcionan para el proposito que yo quiero
            my_file.write(str(1))#le cambio el valor a 1 = encendido #el valor predeterminado con el que empieza el archivo es 0 = apagado
        else:
            await ctx.send("No hay palabras dudosas")
@bot.command(name="6")
async def agregardicpadu(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=991003514010472548#ID espanglish filtrado palabras
    my_file=open("interruptorpdu.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        msg=await ctx.send("Cargando...")
        diccionario.agregar_palabrasddi()
        await msg.edit(content="Se agrego al Diccionario")
@bot.command(name="7")
async def denegarpdu(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=991003514010472548#ID espanglish filtrado palabras
    my_file=open("interruptorpdu.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        diccionario.denegar_palabrad()
        msg=await ctx.send("Cargando...")
        await msg.edit(content="Se denego la palabra")
@bot.command(name="8")
async def mostrarpdu(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=991003514010472548#ID espanglish filtrado palabras
    my_file=open("interruptorpdu.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        pm=diccionario.mostrar_upalabrad()
        await ctx.send(content=f"La palabra dudosa a filtrar es:{pm}")
@bot.command(name="9")
async def apagarinterruptorpdu(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=991003514010472548#ID espanglish filtrado palabras
    my_file=open("interruptorpdu.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID and inter == 1:
        msg=await ctx.send("Cargando...")
        my_file=open("interruptorpdu.txt","w")#abro un archivo y lo uso como intteruptor ya que las variables globales no funcionan para el proposito que yo quiero
        my_file.write(str(0))#le cambio el valor a 1 = encendido #el valor predeterminado con el que empieza el archivo es 0 = apagado
        await msg.edit(content="Saliste del filtrado")
@bot.command(name="mostrardi")
async def mostrardi(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=991003514010472548#ID espanglish filtrado palabras
    my_file=open("interruptorpdu.txt","r")
    inter=int(my_file.read())
    my_file.close()
    if idcanalter==canalID:
        msg=await ctx.send("Cargando...")
        dic=diccionario.mostrar_diccionario()
        await msg.edit(content=f"El diccionario contiene:\n{dic}")
@bot.command(name="mostrar_nuevasp")
async def mostrarnuevasp(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=991003514010472548#ID espanglish filtrado palabras
    if idcanalter==canalID:
        msg=await ctx.send("Cargando...")
        nuevasp=diccionario.mostrar_nuevasp()
        await msg.edit(content=f"Nuevas palabras contiene:\n{nuevasp}")
@bot.command(name="mostrarpdu")
async def mostrarpdu(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=991003514010472548#ID espanglish filtrado palabras
    if idcanalter==canalID:
        vacio=diccionario.mostrar_svacio()
        if vacio==False:
            msg=await ctx.send("Cargando...")
            pdudosas=diccionario.mostrar_palabrasdu()
            await msg.edit(content=f"Palabras dudosas contiene:\n{pdudosas}")
        else:
            await ctx.send("No hay palabras dudosas")
@bot.command(name="mostrarcomandos")
async def mostrarcomandos(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=991003514010472548#ID espanglish filtrado palabras
    if idcanalter==canalID:
        msg=await ctx.send("Cargando...")
        comandos=diccionario.mostrar_comandos()
        await msg.edit(content="Los comandos son:\n")
        for i in range(0,len(comandos)):
            await ctx.send(f"{comandos[i]}\n")
@bot.command(name="mostrarpalabrasde")
async def mostrarpalabrasde(ctx):
    canalID=int(ctx.channel.id)
    idcanalter=991003514010472548#ID espanglish filtrado palabras
    if idcanalter==canalID:
        msg=await ctx.send("Cargando...")
        palabrasde=diccionario.mostrar_palabrasde()
        await msg.edit(content=f"el diccionario contiene:\n{palabrasde}")

@bot.listen()
async def on_message(ctx):
    idautor=ctx.author.id #guarada la id del que mando el mensaje
    
    print(f"El Contenido del mensaje es; {ctx.content.lower()} La id del autor: {ctx.author.id} El Usuario del autor es: {ctx.author.name}")#imprime en la consola el contenido del mensaje, la id de la persona que lo envio y su nombre dde usuario
    canalID=int(ctx.channel.id)#guarda la id del canal donde se envio el mensaje
    idcanal=int(880184945597878388)# id espanglish general-1
    if canalID==idcanal:#compara las id # esto de comparaciones es por los comandos para el filtrado de palabras
        my_file=open("idestudiantes.txt","r")#abre el archivo en modo lectura
        content = my_file.read()#lee el archivo
        my_file.close()#cierra el archivo
        content_list = content.split(', ')#lo separa donde hay ", " y lo guarda en una lista
        removetable = str.maketrans('', '', '[]')#borra los corchetes
        out_list = [s.translate(removetable) for s in content_list]#forma una nueva lista con los datos procesados
        out_list[0]="0"#modifica el subindice 0 porque sino se rompe el archivo
        estaenlista=False#interruptor por si esta en la lista
        for i in range(0,len(out_list)):#comparra para ver si la id esta registrada
            out_list[i]=int(out_list[i])#convierte los str en int para no romper el archivo
            if idautor==out_list[i]:#compara ids
                estaenlista=True#en caso de que se encuentre cambia por el True

        if estaenlista == True:#si esta en la lista
            contmensaje=ctx.content.lower()#guarda lo que dice el mensaje
            epalabra_comando=False#interruptor para ver si el mensaje no es un comando
            palabra_comando=diccionario.palabras_comandos()#llama al metodo palabras_comandos dde diccionario que retorna una lista con los comandos en str
            for i in range(0,len(palabra_comando)):#bucle para la verificacion
                if str(contmensaje)==str(palabra_comando[i]):#compara las palabra de lmensaje con las de los comandos 
                    epalabra_comando=True#en caso de que sea == al comando no se le suma puntos ni se guarda el mensaje
                    break#para salir del bucle una vez encontrado si es un comando
            if epalabra_comando==False:#si la palabraa no es un comando
                verificacion_mensaje=diccionario.buscar_diccionario(contmensaje)#llama al metodo busccar_diccionario para vevr si la palabra esta registrada en el diccionario retora un True, sino guarda la palabra en Nuevas_palabras y retorna un False
                if verificacion_mensaje==True:#si esta en el diccionario
                    usdi=await bot.fetch_user(idautor)#saca el nombre de usuario y el discriminator del usuario que envio el mensaje
                    modificar_exel.cambiar_puntos(usdi.discriminator,contmensaje)#llama el metodo cambiar_puntos de modificar exel y le dad los parametros del discriminator del usuario y el mensaje completo enviado
                    await ctx.add_reaction(emoji="👍")#reacciona al mensaje con este emoji en caso de que estee en el diccionario
                else:
                    await ctx.add_reaction(emoji="🍆")#en caso contrario si no esta en el diccionario reacciona con este emoji
    
    
bot.run("ODU1NTQzNjI0NDI2NTg2MTIy.YM0BFw.ZgQ4UjAuVeYsaQ719mve6UFea_A") #Token bot
