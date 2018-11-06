from Scraper import WebScraper
from Sorter import FileSorter

cars = [
    "Dodge Ram", "Ford F150", "Chevy Silverado", "Tesla Model S",
    "Honda Civic", "Toyota Carolla", "Honda Odyssey", "Dodge Caravan",
    "Toyota Sienna", "Honda CRV", "Jeep Cherokee", "Toyota Rav 4"
]


if __name__ == "__main__":
    fs = FileSorter.FileSorter()
    print(fs.padNumber(9))