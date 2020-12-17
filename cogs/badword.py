import discord
from discord.ext import commands


class BadWord(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Badword is ready.")

    @commands.Cog.listener()
    async def on_message(self, message):
        bad_words = ["nigger", "covid", "school", "project", "porn", "paper",
                     "research", "uwi", "se", "corona", "paul", "walcot",
                     "lowe", "hilary"]

        # dont check for bad words of bot (can lead to infinite loop)
        if message.author == self.client.user:
            return

        def find(msg, bad):  # linear search
            for i in range(0, len(msg)):
                if (msg[i:i+len(bad)] == bad and
                   (i - 1 < 0 or msg[i-1] == ' ') and
                   (i+len(bad) >= len(msg) or msg[i+len(bad)] == ' ')):
                    return True
            return False

        for word in bad_words:
            if find(message.content.lower(), word):
                print("A bad word was said")
                await message.channel.send("\u26A0\uFE0FWARNING\u26A0\uFE0F: A word in your message is not allowed!")
                break


def setup(client):
    client.add_cog(BadWord(client))
