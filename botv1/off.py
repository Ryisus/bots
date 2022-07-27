import os, discord, sys

def restart_bot(id):
    print ("Inicie")
    ingresante = int (id) #ingreso
    print ('ingresante:', ingresante)
    if ingresante == 848254286437023805 or 889604243680530463:# gaucho y jack 
        print ("ingresamos")
        os.execv(sys.executable, ['python'] + sys.argv)#restartea el bot
    else:
        print ('error al reiniciar comprovacion incorrecta')

def den_if():
    async def shutdown(ctx):
        await ctx.send('Apagando ...')
        await ctx.bot.logout()

def off_bot(id):
    print ('go')
    ingreso = int (id)
    print (ingreso)

    print ('go')
    if ingreso == 848254286437023805 or 889604243680530463: # gaucho y jack
        print ('go2')
        den_if()
        print ("go3")

@bot.command(name ="apagar")
async def apagar(ctx):
    id = str(ctx.author.id)
    if id == 848254286437023805 or 889604243680530463: # IDS: Bauti pr Jesus
        await ctx.send("Apagando el bot ...")
        await ctx.bot.logout()
    else:
        await ctx.send("No tienes los permisos suficientes!")


@bot.command(name="start")# para iniciar la contabilidad de mensajes es "start"
async def mensajes(ctx):
    
    id = int(ctx.author.id)
    if id== 848254286437023805 or 367082134927573013:
        await ctx.send("Narnia good")#escribe si es correcto
        #await ctx.send(f"Contenido vector: {str (userMessages)}")#manda el contenido del vector
        await mensaje_hola()
        #on_message()
        #cant=len(userMessages)
        #await ctx.send(f"la cantidad de mensajes son: {cant}") #escribe la cantidad de objetos
    else:
       await ctx.send("Narnia")
    


userMessages = []
userID = 367082134927573013 # Id de la persona
channelID = 897596660002218017 # canal: base_data
#_________________________________________________Esto checkea la ID del user_____________________________________
#cant=0

#______________________________________________