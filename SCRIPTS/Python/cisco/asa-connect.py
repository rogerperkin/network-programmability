import requests 
import json 

url = "https://192.168.1.245/api/routing/static"

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

userpw = ('roger', 'cisco')

get_response = requests.get(
    url, headers=headers, auth=userpw, verify=False).json()['items']

print(json.dumps(get_response, indent=2, sort_keys=True))
