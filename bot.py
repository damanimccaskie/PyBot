
import discord
import time
import asyncio

import image
import flipcoin
import corona

messages = joined = 0

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
    return lines[0].strip()

token = read_token()

client = discord.Client()

async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)


@client.event # This event runs whenever a user updates: status, game playing, avatar, nickname or role
async def on_member_update(before, after): 
    n = after.nick 
    if n: # Check if they updated their username
        if n.lower().count("tim") > 0: # If username contains tim
            last = before.nick
            if last: # If they had a usernae before change it back to that
                await after.edit(nick=last)
            else: # Otherwise set it to "NO STOP THAT"
                await after.edit(nick="NO STOP THAT")


@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    global messages
    messages += 1
    bad_words = ["nigger", "covid", "school", "project", "porn", "paper", "research", "uwi", "SE", "se", "corona"]

    for word in bad_words:
        if message.content == (word):
            print("A bad word was said")
            await message.channel.send("Stop cursing you little fucking nigger!")

    id = client.get_guild(653020828719644683)
    channels = ["commands"]
    
    if message.content == ("~hello"):
      await message.channel.send("Hi and Welcome to \U0001F480 Suicide Race \U0001F480") 
    elif message.content == "~users":
      await message.channel.send(f"""Number of Members: {id.member_count}""")
    elif message.content == "~drive":
      await message.channel.send("https://drive.google.com/drive/folders/12f2grZf1lycx9Iz-dKbFtFbMLgsJHlUy")
    elif message.content == "prefix":
      await message.channel.send("The Prefix is '~'")
    elif message.content == ("corona"):
      await message.channel.send("\u26A0 CORONA DETECTED \u26A0 Contact (246)-536-4500 NOW If You Or Anyone You Know Has The Virus")
    elif message.content.startswith("~image"):
      await image.run(message)
    elif message.content == "~flipcoin":
      await flipcoin.run(message)
    elif message.content.startswith("~cstats"):
      await corona.run(message)
    
      
    if message.content == "~help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="~hello", value="Greets the user")
        embed.add_field(name="~users", value="Prints number of users")
        embed.add_field(name="~drive", value="Prints link to SR Drive")
        embed.add_field(name="~image", value="Shows specified image")
        embed.add_field(name="~flipcoin", value="Flips a coin (heads / tails)")
        embed.add_field(name="~cstats", value="Displays COVID-19 information with specified country.")
        await message.channel.send(content=None, embed=embed)

    
    if message.content == "~covid":
        cov_embed = discord.Embed(title ="\U0001F9A0 Coronavirus/COVID-19 Information", description= "\U0001F1E7\U0001F1E7 Barbados Coronavirus/COVID-19 Information")
        cov_embed.add_field(name = ":syringe:Tested:", value="694(+92)")
        cov_embed.add_field(name = ":white_check_mark:Confirmed:", value="66(+3)")
        cov_embed.add_field(name = ":heart:Recovered:", value="11(+3)")
        cov_embed.add_field(name = ":skull:Deaths:", value="3")
        cov_embed.add_field(name = ":arrow_forward:Active Cases:", value="52(+3)(-3)")
        cov_embed.add_field(name = ":x:Critical:", value="4")
        cov_embed.add_field(name = ":baby:Youngest Case:", value="7")
        cov_embed.add_field(name = ":older_man:Oldest Case:", value="95")
        cov_embed.add_field(name = ":mens:Males:", value="32")
        cov_embed.add_field(name = ":womens:Females:", value="34")
        cov_embed.add_field(name = ":mag:Under Investigation:", value="-")
        cov_embed.add_field(name = ":question:Other Facts:", value= ":one: First Case was recorded on 17th March 2020. \n :two: Stage 3 was implemented on 26th March 2020 (Curfew from Saturday, March 28, to Tuesday, April 14, 8:00 p.m. to 6:00 a.m). \n :three: 24-hour curfew was issued 3rd April 2020 to 14th April 2020.")
        await message.channel.send(content=None, embed = cov_embed)

client.loop.create_task(update_stats())
client.run(token)
