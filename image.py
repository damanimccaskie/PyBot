import requests
import discord
from bs4 import BeautifulSoup
from random import choice


async def run(main):
    args = main.content.split(" ")  # split message into a list by spaces

    search = ""
    for i in range(1, len(args)):
        # concat the words as a search string (with + for url)
        search += args[i] + "+"
    search = search.strip()  # trim off whitespace from font and back of string
    search = search[:len(search) - 1]  # remove the last , (it not needed)

    # if user doesnt enter a search phrase
    default = ["random", "meme", "suicide", "corona", "pepe julian onziema"]

    headers = {
        "Accept": "text/html",
        "User-Agent": "Mozilla/5.0 (X11; Linux i586; rv:31.0) " +
        + " Gecko/20100101 Firefox/71.0"
    }

    url = "http://results.dogpile.com/serp?qc=images&q=" + (choice(default)
                                                            if len(search) < 1
                                                            else search)
    page = requests.get(url, headers=headers)  # raw page
    dom = BeautifulSoup(page.content, "html.parser")  # beautified dom
    links = dom.select(".image a.link")  # parse out img
    # get all the links from the a's using list comprehension
    urls = [i["href"] for i in links]

    if len(urls) < 1:  # no image results found
        await main.channel.send(":x: Couldn't find any images that match " +
                                + "that description... srry :x:")
        print("No results")
        return

    # post image to chat
    embed = discord.Embed(title="Image", description="your image",
                          color=0x33ffff)
    # randomly choose one of the image results to post
    embed.set_thumbnail(url=choice(urls))
    await main.channel.send(content=None, embed=embed)
