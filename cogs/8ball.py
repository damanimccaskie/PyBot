# import discord
import random
from discord.ext import commands


class _8ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("8ball is ready.")

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        """Ask 8Ball a question."""
        responses = ['It is certain.', 'It is decidedly so.',
                     'Without a doubt.', 'Yes definitely.',
                     'You may rely on it.', 'As I see it, yes.',
                     'Most likely.', 'Outlook good.', 'Yes.',
                     'Signs point to yes.', 'Reply hazy, try again.',
                     'Ask again later', 'Better not tell you now.',
                     'Cannot predict now.', 'Concentrate and ask again.',
                     'Do Not count on it.', 'My reply is no.',
                     'My sources say no.', 'Outlook not so good.',
                     'Very doubtful']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(client):
    client.add_cog(_8ball(client))
