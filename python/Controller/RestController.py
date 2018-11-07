import json
import random

import numpy as np
import requests
from flask import Flask, request

from agents import Collector
from ai_model import image_predict
from model import models
from Scraper.WebScraper import WebScraper

app = Flask(__name__)

@app.route('/call-tensor-flow', methods=["POST"])
def getConfidence():
    filename  = request.json["filename"]
    tfData = image_predict(filename)
    out = json.dumps(tfData)
    return str(out)

@app.route('/recommend', methods=["POST"])
def getRecommendations():
    carName = request.json["carname"]
    collector = Collector.Collector(carName)
    return json.dumps(collector.collect(carName))
