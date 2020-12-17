import discord
import random
from discord.ext import commands
from random import choice


class FlipCoin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Image is ready.")
    
    @commands.command(aliases=['flip'])
    async def flipcoin(self, ctx):
        """Flips a virtual coin."""
        options = ["HEADS \U0001F642", "TAILS \U0001F643"]
        await ctx.channel.send(choice(options))


def setup(client):
    client.add_cog(FlipCoin(client))