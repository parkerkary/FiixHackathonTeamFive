from Scraper.WebScraper import WebScraper
from Controller import RestController

if __name__ == "__main__":
    RestController.app.run(host="0.0.0.0",port="8080")