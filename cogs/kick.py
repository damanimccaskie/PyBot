import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Kick is ready.")

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks a specified user."""
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked from the server!')


def setup(client):
    client.add_cog(Kick(client))