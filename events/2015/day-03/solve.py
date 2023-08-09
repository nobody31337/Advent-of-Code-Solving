import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/3/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

directions = response.text

cur = [0, 0]
path = [[*cur]]

for d in directions:
    match d:
        case '>':
            cur[0] += 1
        case '<':
            cur[0] -= 1
        case '^':
            cur[1] += 1
        case 'v':
            cur[1] -= 1
    if cur not in path:
        path.append([*cur])

print(len(path))
