import requests
from bs4 import BeautifulSoup
import re


def removeNones(arr):
    while (None in arr):
        arr.remove(None)


def isVisible(element):
    if element.parent.name in [
            'style', 'script', '[document]', 'head', 'title'
    ]:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    if (element == "\n"):
        return False
    return True


def cleanLink(link):
    link = link[7:]
    splitChar = "&"
    if ".html" in link:
        splitChar = ".html"
    elif ".htm" in link:
        splitChar = ".htm"
    link = link.split(splitChar)
    if(splitChar == "&"):
        return link[0]
    else:
        return link[0] + splitChar


def extractWords(sentence):
    if (sentence == "\n"):
        return False
    else:
        return sentence.split()


class WebScraper:
    def __init__(self, vehicleName):
        self.vehicleName = vehicleName
        self.urls = self.rmGoogle(vehicleName, 5)
        self.goodUrls = self.filterUrls()
        self.scores = [x["score"] for x in self.goodUrls]
        self.webpage = self.goodUrls[self.scores.index(max(self.scores))]["url"]

    def google(self, searchQuery, count):
        page = requests.get("https://www.google.com/search?q=" + searchQuery)
        soup = BeautifulSoup(page.content, "lxml")
        result_divs = soup.findAll('div', {'class': 'g'})[:count + 1]
        links = [div.find('a') for div in result_divs]
        removeNones(links)
        hrefs = [cleanLink(link.get('href')) for link in links]
        return list(set(hrefs))

    def rmGoogle(self, searchQuery, count):
        searchQuery = "Recommended 'maintenance' for " + searchQuery
        searchString = "+".join(searchQuery.split())
        return self.google(searchString, count)

    def getTitle(self, url):
        try:
            html = requests.get(url)
        except:
            return ""
        soup = BeautifulSoup(html.content, "lxml")
        if(soup.title):
            return soup.title.string
        else:
            return ""

    def getH1(self, url):
        try:
            html = requests.get(url)
        except:
            return []
        soup = BeautifulSoup(html.content, "lxml")
        headers = soup.find_all("h1", limit=6)
        headText = [x.text.strip() for x in headers]
        return headText

    def makeURlObj(self, url):
        urlDict = {}
        urlDict["url"] = url
        urlDict["title"] = self.getTitle(url)
        urlDict["headers"] = self.getH1(url)
        return urlDict

    def filterUrls(self):
        urlObjs = []
        for url in self.urls:
            if "auto123" in url:
                self.urls.remove(url)
            else:
                urlDict = self.makeURlObj(url)
                urlDict["score"] = 0
                for word in self.vehicleName.split():
                    if (word in url or word in urlDict["title"]):
                        urlDict["score"] += 1
                    for header in urlDict['headers']:
                        if (word in header):
                            urlDict["score"] += 1
                urlObjs.append(urlDict)
        return urlObjs
