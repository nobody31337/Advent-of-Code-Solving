import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/8/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

strings = response.text.splitlines()

partone = 0

for string in strings:
    partone += len(string) - len(string[1:-1].encode().decode('unicode_escape'))
    print(string.encode('unicode_escape'))

print(partone)