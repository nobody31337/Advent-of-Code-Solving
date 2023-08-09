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

print(hashlib.md5(b'abcdef609043').hexdigest())