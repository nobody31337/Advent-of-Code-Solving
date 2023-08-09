import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/6/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

inst = response.text.split('\n')

for step in inst[:-1]:
    fx, fy = map(int, step.split()[-3].split(','))
    
    tx, ty = map(int, step.split()[-1].split(','))

    print(fx, fy, tx, ty)

    if step.startswith('turn on'):
        pass
    if step.startswith('turn off'):
        pass
    if step.startswith('toggle'):
        pass