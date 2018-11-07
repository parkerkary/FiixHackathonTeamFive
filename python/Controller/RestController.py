from flask import Flask, request
import requests
import random
from Scraper.WebScraper import WebScraper
from model import models
import json
import numpy as np
from agents import Collector
from ai_model import image_predict

app = Flask(__name__)
sageMakerAddress = "http://127.0.0.1:5000/mock-sage-maker"

Cars = models.keys()
numCars = len(Cars)
print(Cars)

def callTensorFlow(filename):
    out = image_predict(filename)
    return json.dumps(out)
    

def getLink(carName):
    ws = WebScraper(carName)
    return ws.webpage


@app.route('/call-tensor-flow', methods=["POST"])
def getConfidence():
    content = request.json
    tfData = callTensorFlow(content["filename"])
    return str(tfData)

@app.route('/recommend', methods=["POST"])
def getRecommendations():
    collector = Collector.Collector()
    return json.dumps(collector.collect(1))