from Scraper.WebScraper import WebScraper
import sys
cars = [
    "Dodge Ram", "Ford F150", "Chevy Silverado", "Tesla Model S",
    "Honda Civic", "Toyota Carolla", "Honda Odyssey", "Dodge Caravan",
    "Toyota Sienna", "Honda CRV", "Jeep Cherokee", "Toyota Rav 4"
]

def test():
    out = True
    for x in cars:
        try:
            ws = WebScraper(x)
            out = out and ws.webpage 
        except:
            return False
    return out

if __name__ == "__main__":
    name = ""
    for x in range(len(sys.argv)-1):
        name  = name + sys.argv[x+1] + " "
    print(name)
    ws = WebScraper(name)
    print(ws.webpage)
    # if(test()):
    #     print("Webscraper Test Passed")
    # else:
    #     print("Webscraper Test Failed")
