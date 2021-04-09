# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

#PREFIX
prefix= os.getenv('PREFIX')

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
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the game"))
    print(f'{client.user} Se conectó a discord!')

client.run(os.getenv('TOKEN'))

