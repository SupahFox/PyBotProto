# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


#CLIENT
client = discord.Client()

#ENV
load_dotenv()
prefix = os.getenv('PREFIX')
token = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

#COMMANDS
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(prefix + 'hello'):
    await message.channel.send('Hello!')

  if message.content.startswith(prefix + 'reason'):
    await message.channel.send('Esto es una prueba de la libreria discord.py que posiblemente se agregue al bot principal. Ignoren esto.')

#READY
@client.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='the game'), status=discord.Status.do_not_disturb)
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the game"))
    print(f'{client.user} Se conectó a discord!')

    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} está conectado a la siguiente guild:\n'
        f'{guild}(id: {guild.id})'
    )

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

        
client.run(token)

