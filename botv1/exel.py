import os, discord, sys, random, time, logging
from turtle import delay, title
from discord.ext import commands, flags
import pandas as pd
import time
# import off

client = discord.Client()
guild = discord.Guild

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
        print('\nBot iniciado!') # mira el comentario abajo
        await bot.change_presence (activity=discord.Activity(type=discord.ActivityType.watching,name=' HolaSoyGerman ')) # Esto es para poner el estado del bot

while (1):
    @client.event
    async def on_message(message):
        if message.user == client.user:
            return
        elif message.content.startswith('_'):

            cmd = message.content.split()[0].replace("_","")
            if len(message.content.split()) > 1:
                parameters = message.content.split()[1:]
        print(cmd)

        if cmd == 'scan':

            data = pd.DataFrame(columns=['content', 'time', 'author']) #arma columnnas en un archivo similar a exel. <

            def is_command (msg): # Checking if the message is a command call
                if len(msg.content) == 0:
                    return False
                elif msg.content.split()[0] == '_scan':
                    return True
                else:
                    return False

            limit=0

            async for msg in message.channel.history(limit=10000):
                if msg.author != client.user:
                    if not is_command(msg):
                        data = data.append({'content': msg.content, #guarda todo esto en el archivo del exel
                                            'time': msg.created_at,
                                            'author': msg.author.name}, ignore_index=True)
                    if len(data) == limit:
                        break

            file_location = "data.csv" # archivo guarda y localiza el archivo
            
            data.to_csv(file_location)

async def mensaje_hola():
     contador=int(0)
     print("dentro de la funcion")
     if message.content.startswith('sape'):
         contador=contador+1
         channel = message.channel
         await channel.send('Perfect')
         await channel.send(str(contador))

async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Bienvenido {0.mention} a {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
            # esto lo saque de la guia de discord.py

# comandos


def restart_bot(): #para reiniciar bot linea 51
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(name ="reiniciar")
async def reiniciar(ctx):
    id = int(ctx.author.id)
    if id == 848254286437023805 or 367082134927573013 or 900501480946139167: # IDS: Bauti pr Jesus
        await ctx.send("Reiniciando el bot...")
        restart_bot()
    else:
        await ctx.send("No tienes los permisos suficientes!")

@bot.command(name ="restart")
async def reiniciar2(ctx):
    id = int(ctx.Role.id)
    if id == 897631749356552242 : # IDS: Bauti pr Jesus
        await ctx.send("Reiniciando el bot...")
        restart_bot()
    else:
        await ctx.send("No tienes los permisos suficientes!")

@bot.command(name= 'ping')
async def ping(ctx):
    antes = time.monotonic()
    m=await ctx.send('Pong!')
    p1=(time.monotonic()-antes)*1000 #variable de tiempo
    p2=(str(p1).split('.'))[0]#para escribir nomas
    await m.edit(content=f'Pong! (ms={p2})')

@bot.command(name= 'sex')
async def sex(ctx):
    await ctx.message.add_reaction(emoji="🍆")
    await ctx.message.add_reaction(emoji="🍑")

@bot.command(name="sexo")
async def sexo(ctx):
    message= "**SEXOO**"
    react_messasge = await ctx.send(message)
    await react_messasge.add_reaction(emoji="🍆")
    await react_messasge.add_reaction(emoji="🍑")


@bot.listen()
async def on_message(message):
    contadormensaje=int(0)
    #mensajes=await ctx.message.content()
    if "start" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('lo lei')
        #mensajes.append(message.content)
        #await message.channel.send(len(mensajes))
        #await bot.process_commands(message)



bot.run("ODU1NTQzNjI0NDI2NTg2MTIy.YM0BFw.ZgQ4UjAuVeYsaQ719mve6UFea_A") #api bot
