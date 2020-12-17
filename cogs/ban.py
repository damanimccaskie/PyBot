import discord
from discord.ext import commands


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ban is ready.")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Specify a user to ban."""
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned from the server!')


def setup(client):
    client.add_cog(Ban(client))