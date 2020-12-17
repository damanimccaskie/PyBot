import discord
from discord.ext import commands


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Clear is ready.")
  
    @commands.command(aliases=['purge'])
    async def clear(self, ctx, amount=5):
        """Clears a specified amount of messages."""
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(Clear(client))