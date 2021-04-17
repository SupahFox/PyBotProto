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

  if message.content.startswith(prefix + 'gabito'):
    embed=discord.Embed(title="si", description="si", color=discord.Colour.blue())
    embed.set_image(url="https://cdn.discordapp.com/attachments/671170382010515466/774014254286110770/Troll_face.png")
    embed.set_footer(text="chupame la pija bobo")
    await message.channel.send(embed=embed)
#READY
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name='the game'))
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

