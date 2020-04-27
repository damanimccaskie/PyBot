from random import choice

async def run(main):
    options = ["HEADS \U0001F642", "TAILS \U0001F643"]
    await main.channel.send(choice(options))