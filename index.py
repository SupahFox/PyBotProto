#IMPORTAR LIBRERIAS
import discord 
from discord.ext import commands

#PREFIX
bot= commands.Bot(command_prefix='py!')

#PING
@bot.command()
async def test(ctx):
    await ctx.send('Esto es una prueba de la libreria discord.py que posiblemente se agregue al bot principal. Ignoren esto.')
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the game"))
    print('Listo')
#TOKEN
bot.run('TOKEN')
