import requests
import json
import os
import sys

#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ._lib import convJson

url = "http://192.168.11.122:8888/inference"

def call(data: str) -> any:
    payload = {'data': data}
    r = requests.post(url, data=payload)
    return r

def npToJson(data):
    return json.dumps(data, cls=convJson.NumpyArrayEncoder)
