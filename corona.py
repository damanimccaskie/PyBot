from bs4 import BeautifulSoup
import discord
import re
import requests


def getRegion(l, r):
    for i in l:
        # case insenstive comparison
        if ((i.get("Country, Other") or
             i.get("USA State")).lower() == r.lower()):
                return i


def joinMsg(words):
    phrase = ""
    for i in range(1, len(words)):
        phrase += words[i]
    phrase = phrase.strip()  # trim off whitespace from font and back of string
    return phrase


def extract_from_tag(tag, line):
    regex = r'(<'+tag+'[^>]*>)'

    line = line[re.search(regex, line).span()[1]:-5].replace("\n", "")
    line = line.replace("\xa0", " ")
    line = line.replace("<nobr>1M pop</nobr>", "1M pop").replace('<br>', ' ')
    return line.replace("</br>", "").replace("<br/>", " ")


def parseTable(url, ID, first):
    headers = {
        "Accept": "text/html",
        "User-Agent": "Mozilla/5.0 (X11; Linux i586; rv:31.0) " +
        + "Gecko/20100101 Firefox/71.0"
    }

    page = requests.get(url, headers=headers)  # raw page
    dom = BeautifulSoup(page.content, "html.parser")  # beautified dom
    table = dom.find('table', attrs={'id': ID}).findAll("tbody")[0]
    tableHead = dom.find('table', attrs={'id': ID}).findAll("thead")[0]

    start = False
    indexed = False
    list_of_rows = []
    headings = [extract_from_tag("th", str(th))
                for th in tableHead.findAll('th')[0:]]

    for row in table.findAll('tr')[0:]:
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace(' ', '')
            list_of_cells.append(text.strip())
        indexed = list_of_cells[0] == '' or list_of_cells[0].isnumeric()
        if list_of_cells[1 if indexed else 0] == first:
            start = True
        if start:
            region = dict()
            for h, i in zip(headings, range(0, len(headings))):
                region[h] = list_of_cells[i]
            list_of_rows.append(region)
    return list_of_rows


async def run(main):
    args = main.content.split(" ")  # split message into a list by spaces

    region = "World" if len(args) < 2 else joinMsg(args)

    urlsId = (("https://www.worldometers.info/coronavirus/",
              "main_table_countries_today", "World"),
              ("https://www.worldometers.info/coronavirus/country/us/",
               "usa_table_countries_today", "USATotal"))

    rows = []
    for url, ID, first in urlsId:
        rows += parseTable(url, ID, first)

    '''0 - country, 1 - total cases, 2 - new cases, 3 - total deaths,
       4 - new deaths, 5 - total recovered, 6 - active cases,
       7 - serious critical, 8 - total cases / 1m pop, 9 - deaths / 1m pop,
       10 - total tests, 11 - total test / 1m pop'''

    info_embed = discord.Embed(title="\U0001F9A0 COVID-19 Information",
                               description="Numero Uno Fuente Por " +
                               + "Informacion de COVID-19")

    data = getRegion(rows, region)
    if data:
        for heading in data:
            if heading == "Source" or heading == "Projections":
                continue
            info_embed.add_field(name=heading, value=data[heading]
                                 if len(data[heading]) > 0 else "-")
        await main.channel.send(content=None, embed=info_embed)
    else:
        await main.channel.send(":no_entry_sign: Sorry we have no data " +
                                + "for that region. Please try again! " +
                                + ":no_entry_sign:")
