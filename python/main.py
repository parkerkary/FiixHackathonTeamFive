from Scraper.WebScraper import WebScraper
cars = [
    "Dodge Ram", "Ford F150", "Chevy Silverado", "Tesla Model S",
    "Honda Civic", "Toyota Carolla", "Honda Odyssey", "Dodge Caravan",
    "Toyota Sienna", "Honda CRV", "Jeep Cherokee", "Toyota Rav 4"
]


if __name__ == "__main__":
    print("Welcom to the Main Method\n")
    ws = WebScraper("Jeep Cherokee")
    print(ws.webpage)
    # for x in cars:
    #     ws = WebScraper(x)
    #     print(ws.webpage)