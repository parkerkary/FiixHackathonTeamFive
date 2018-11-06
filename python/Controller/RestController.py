from flask import Flask, request
import requests
import random
from Scraper.WebScraper import WebScraper
from model import models
import json
import numpy as np
from agents import Collector
app = Flask(__name__)
sageMakerAddress = "http://127.0.0.1:5000/mock-sage-maker"

Cars = models.keys()
numCars = len(Cars)
print(Cars)

def callTensorFlow(content):
    r = requests.post(sageMakerAddress,data=content)
    j = json.loads(r.content)
    numpyJ = np.array(j["data"])
    largest = numpyJ.argsort()[-5:][::-1]
    out = []
    for x in largest:
        obj = {}
        obj["name"] = Cars[x]
        obj["confidence"] = j["data"][x]
        out.append(obj)
    return json.dumps(out)
    

def getLink(carName):
    ws = WebScraper(carName)
    return ws.webpage


@app.route('/call-tensor-flow', methods=["POST"])
def getConfidence():
    content = request.json
    tfData = callTensorFlow(content)
    return str(tfData)

# Mock
@app.route('/mock-sage-maker', methods=["POST"])
def getResults():
    randoms = [random.randint(0,100) for x in range(numCars)]
    _sum = float(sum(randoms))
    out = { "data": [x/_sum for x in randoms]}
    return json.dumps(out)

@app.route('/recommend', methods=["POST"])
def getRecommendations():
    collector = Collector.Collector()
    return json.dumps(collector.collect(1))