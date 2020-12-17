import discord
from discord.ext import commands


class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Unban is ready.")


    @commands.command()
    async def unban(self, ctx, *, member):
        """Unbans a specified user."""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
           user = ban_entry.user

           if(user.name, user.discriminator) == (member_name, member_discriminator):
             await ctx.guild.unban(user)
             await ctx.send(f'Unbanned {user.mention}')
             return


def setup(client):
    client.add_cog(Unban(client))