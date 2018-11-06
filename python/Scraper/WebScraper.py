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
    if(element == "\n"):
        return False
    return True


def cleanLink(link):
    link = link[7:]
    link = link.split(".htm")
    return link[0] + ".htm"

def extractWords(sentence):
    if(sentence == "\n"):
        return False
    else:
        return sentence.split()


class WebScraper:
    # urls: List<string>

    keywords = [
        "Maintenance", "Scheduled", "Schedule", "Service", "Check", "Inspect",
        "Tighten", "Complete", "Replace", "Test", "Rotate", "Set", "Reset",
        "Engine", "Oil", "Brake", "Tire", "Fuel", "Transmission"
    ]

    text_elements = ["div", "p", "td", "tr", "th", "span", ""]

    def __init__(self, vehicleName):
        print("initialized")
        self.vehicleName = vehicleName
        self.urls = self.rmGoogle(vehicleName, 5)
        self.filterUrls()
        for x in self.urls:
            print x
        # self.scores = self.getScores()
        # self.webpage = self.getMostValid()

    def google(self, searchQuery, count):
        page = requests.get("https://www.google.com/search?q=" + searchQuery)
        soup = BeautifulSoup(page.content, "lxml")
        result_divs = soup.findAll('div', {'class': 'g'})[:count+1]
        links = [div.find('a') for div in result_divs]
        removeNones(links)
        hrefs = [cleanLink(link.get('href')) for link in links]
        return list(set(hrefs))

    def rmGoogle(self, searchQuery, count):
        searchQuery = "Recommended 'maintenance' for " + searchQuery
        searchString = "+".join(searchQuery.split())
        return self.google(searchString, count)

    def filterUrls(self):
        names = self.vehicleName.split()

    def getWords(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "lxml")
        data = soup.findAll(text=True)
        result = filter(isVisible, data)
        superResult = []
        for x in result:
            superResult += [word.lower() for word in x.split()]
        return superResult

    def getScores(self):
        output = []
        for url in self.urls:
            count = 0
            words = self.getWords(url)
            for keyword in self.keywords:
                count+= words.count(keyword.lower())
            output.append(count)
        return output

    def getMostValid(self):
        return self.urls[self.scores.index(max(self.scores))]