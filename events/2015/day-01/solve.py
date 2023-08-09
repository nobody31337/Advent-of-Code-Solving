import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/1/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

inst = response.text

print(inst.count('(') - inst.count(')'))

for i in range(len(inst)):
    if inst[:i+1].count('(') - inst[:i+1].count(')') == -1:
        print(i+1)
        break