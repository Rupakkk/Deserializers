import json
import requests
from rest_framework import renderers
import json

URL = "http://127.0.0.1:8000/stucreate/"
data = {
    'name':'Ram',
    'age':25,
    'address':'Ktm'
}

json_data = json.dumps(data)
r = requests.post(url = URL,data = json_data)
data = r.json()