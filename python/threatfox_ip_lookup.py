import requests
import json

url = 'https://threatfox-api.abuse.ch/api/v1/'

with open('connected_ips') as f:
    lines = f.read().splitlines()

potential_threat = {}
for ip in lines:
    obj = {'query': 'search_ioc', 'search_term': ip}
    # print(obj)
    response = requests.post(url, data=json.dumps(obj))
    print(response.text)
    print(ip)
    if "ioc" in response.text:
        potential_threat[ip] = response.json()
        print(ip)

# Writes potential_threat to JSON file
with open('jsonThreatInfo.json', 'w') as outfile:
    json.dump(potential_threat, outfile)
