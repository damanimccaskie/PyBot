from random import choice

async def run(main):
    options = ["HEADS", "TAILS"]
    await main.channel.send(choice(options))