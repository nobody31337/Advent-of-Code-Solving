import requests
import json
import hashlib

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/4/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

content = response.content.strip()
i=1

while True:
    if hashlib.md5(content + str(i).encode()).hexdigest().startswith('00000'):
        break
    i+=1

print(content + str(i).encode())