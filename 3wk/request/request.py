import requests
import json
import pprint
import time

get = requests.get('http://localhost:9000/receive', params=None)

getJsonText = get.text
getJson = json.loads(getJsonText)
pprint.pprint(getJson)

print()

post = requests.post('http://localhost:9000/receive', data=None, json=None)

postJsonText = post.text
postJson = json.loads(postJsonText)
pprint.pprint(postJson)