from random import choice

async def run(main):
    options = ["HEADS :simple_smile:", "TAILS \U0001F643"]
    await main.channel.send(choice(options))