from bs4 import BeautifulSoup
import requests
import re


def getData(url):
    return BeautifulSoup(url, 'html.parser')


def transformData(name):
    data = re.search(r'(\d{4}).*?([A-Z].*)\.', name)
    if(not data):
        name = name.replace("\n", "##")
        data = re.search(r"^(\d{4}).*([A-Z].*?)$", name, re.MULTILINE)
    return {"ano": data.group(1), "nomes": data.group(2).split("##")}


def getBirthdays(data):
    soup = getData(re.search(r'Nascimentos<\/span><\/h2>(.*?)<h2>', requests.get(
        "https://pt.wikipedia.org/wiki/{}".format(data)).text, re.MULTILINE | re.DOTALL).group(1))
    return [transformData(item.text) for item in soup.find_all('li')
            if(re.match(r'\d{4}', item.text[:4]))]


def getDeaths(data):
    soup = getData(re.search(r'Mortes<\/span><\/h2>(.*?)<h2>', requests.get(
        "https://pt.wikipedia.org/wiki/{}".format(data)).text, re.MULTILINE | re.DOTALL).group(1))
    return [transformData(item.text) for item in soup.find_all('li')
            if(re.match(r'\d{4}', item.text[:4]))]


def getEventosHistoricos(data):
    soup = getData(re.search(r'históricos<\/span><\/h2>(.*?)<h2>', requests.get(
        "https://pt.wikipedia.org/wiki/{}".format(data)).text, re.MULTILINE | re.DOTALL).group(1))
    return [transformData(item.text) for item in soup.find_all('li')
            if(re.match(r'\d{4}', item.text[:4]))]
