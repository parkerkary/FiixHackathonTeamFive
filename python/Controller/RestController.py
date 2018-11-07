import json
import random

import numpy as np
import requests
from flask import Flask, request, Response

from agents import Collector
from ai_model import label_image
from Scraper.WebScraper import WebScraper

app = Flask(__name__)

@app.route('/call-tensor-flow', methods=["POST"])
def getConfidence():
    filename  = request.json["filename"]
    tfData = label_image.image_predict(filename)
    prettyData = {}
    for x in tfData:
        prettyData["name"] = tfData[x]["name"].title()
        prettyData["confindence"] = tfData[x]["confidence"]
    out = json.dumps(prettyData)
    return Response(out, mimetype='application/json')

@app.route('/recommend', methods=["POST"])
def getRecommendations():
    carName = request.json["carname"]
    collector = Collector.Collector(carName)
    out =json.dumps(collector.collect(carName))
    return Response(out, mimetype='application/json')
