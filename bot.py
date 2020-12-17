import discord
# import random
import os
# import json
from discord.ext import commands, tasks
from itertools import cycle


messages = 0
status = cycle(['with .help', 'with yo Momma!', 'with Death!', 'with COVID!'])

# def get_prefix(client, message):
#   with open("prefixes.json", "r") as f:
#     prefixes = json.load(f)

#   return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix='.')
#client = commands.Bot(command_prefix = get_prefix)



#cogs


@client.command()
async def load(ctx, extension):
    """Loads a command."""
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    """Unloads a command."""
    client.unload_extension(f"cogs.{extension}")


def loadAll():
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            client.load_extension(f"cogs.{filename[:-3]}")


loadAll()

#events


@client.event
async def on_ready():
    change_status.start()
    print("Bot is ready.")


@client.event
async def on_member_join(member): print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member): print(f'{member} has left the server.')
    

# @client.event
# async def on_guild_join(guild):
#    with open("prefixes.json", "r") as f:
#     prefixes = json.load(f)

#    prefixes[str(guild.id)] = '.'

#    with open("prefixes.json", "w") as f:
#      json.dump(prefixes, f, indent=4)

# @client.event
# async def on_guild_remove(guild):
#   with open("prefixes.json", "r") as f:
#     prefixes = json.load(f)

#   prefixes.pop(str(guild.id))

#   with open("prefixes.json", "w") as f:
#     json.dump(prefixes, f, indent=4)



# #commands
# @client.command()
# async def changeprefix(ctx, newprefix):
#     with open("prefixes.json", "r") as f:
#       prefixes = json.load(f)

#     prefixes[str(ctx.guild.id)] = newprefix

#     with open("prefixes.json", "w") as f:
#       json.dump(prefixes, f, indent=4)
       
#     await ctx.send(f"Prefix changed to: {newprefix}")

#Note to self .... * means to take in all arguments after, as one string
#tasks
@tasks.loop(seconds=1800)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))

client.run('NzE0NTI0MjE0NDM4MTMzNzYw.Xsv6hw.j(HACK)JDZy_QiIKUNH7aGDBM9XbJ7MY8')
