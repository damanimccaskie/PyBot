import requests
import discord
from bs4 import BeautifulSoup

def getRegion(l, r):
    for i in l:
        if i[0].lower() == r.lower(): #case insenstive comparison
            return i


async def run(main):
    args = main.content.split(" ") #split message into a list by spaces

    region = "World" if len(args) < 2 else args[1]

    headers = { 
        "Accept": "text/html",
        "User-Agent": "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/71.0"
    }

    url = "https://www.worldometers.info/coronavirus/"
    page = requests.get(url, headers=headers) #raw page
    dom = BeautifulSoup(page.content, "html.parser") #beautified dom
    table = dom.find('table', attrs={'id': 'main_table_countries_today'}).findAll("tbody")[0]

    start = False
    list_of_rows = []
    for row in table.findAll('tr')[0:]:
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace(' ', '')
            list_of_cells.append(text)
        if list_of_cells[0] == "World":
            start = True
        if start:
            list_of_rows.append(list_of_cells[:-1])
    
    '''0 - country, 1 - total cases, 2 - new cases, 3 - total deaths, 4 - new deaths, 5 - total recovered
    6 - active cases, 7 - serious critical, 8 - total cases / 1m pop, 9 - deaths / 1m pop,
    10 - total tests, 11 - total test / 1m pop'''

    info_embed = discord.Embed(title ="\U0001F9A0 Coronavirus/COVID-19 Information", description= "\U0001F1E7\U0001F1E7 Corona info worldwide")

    headings = ["country", "total cases", "new cases", "total deaths", "new deaths", "total recovered",
    "active cases", "serious, critical", "total cases / 1m pop", "deaths / 1m pop", "total tests",
    "total tests / 1m pop"]

    data = getRegion(list_of_rows, region)
    if data:
        for h, v in zip(headings, data):
            info_embed.add_field(name = h, value = v if len(v) > 0 else "-")
        await main.channel.send(content=None, embed=info_embed)
    else:
        await main.channel.send("Seems we have no data for that region")