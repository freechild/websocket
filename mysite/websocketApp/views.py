from django.shortcuts import render
from .models import *
from .websocket import *
import websocket
import json
import sys

client = mongo_connect('localhost',27017,'btc-database','test.ok_sub_spot_btc_usd_ticker')

def index(request):
    data = findAll(client,'polls')
    return render(request, "index.html",data)


