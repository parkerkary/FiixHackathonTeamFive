from flask import {
    Flask,
    request
}
from Scraper.WebScraper import WebScraper
app = Flask(__name__)


@app.route('/call-tensor-flow', methods=["POST"])
def getConfidence():
    content = request.json
    tfData = callTensorFlow(content)
    return 1


def callTensorFlow(content):
    print(content)
    return content == "hello_world"

def getLink(carName):
    ws = WebScraper(carName)
    return ws.webpage