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

@app.route('/recommend/<carName>', methods=["POST"])
def getRecommendations():
    collector = Collector.Collector()
    return json.dumps(collector.collect(request.view_args['carName']))
