# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.author == client.user:
    return

  if message.content.startswith('py!hello'):
    await message.channel.send('Hello!')

@client.event
async def on_ready():
    print(f'{client.user} Se conectó a discord!')

client.run(os.getenv('TOKEN'))

