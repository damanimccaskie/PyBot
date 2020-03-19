# bot.py
import os
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
    print(f"{client.user} has connected to Discord!")

client.run(TOKEN)
