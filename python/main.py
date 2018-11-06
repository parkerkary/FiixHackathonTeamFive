import sys
from Scraper.WebScraper import WebScraper

cars = [
    "Dodge Ram", "Ford F150", "Chevy Silverado", "Tesla Model S",
    "Honda Civic", "Toyota Carolla", "Honda Odyssey", "Dodge Caravan",
    "Toyota Sienna", "Honda CRV", "Jeep Cherokee", "Toyota Rav 4"
]


if __name__ == "__main__":
    name = ""
    for x in range(len(sys.argv)-1):
        name += sys.argv[x+1] + " " 
    print "scraping for " + name
    ws = WebScraper(name)
    print(ws.webpage)