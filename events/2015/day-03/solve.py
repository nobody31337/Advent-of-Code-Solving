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
santa = [[*cur]]

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
    if cur not in santa:
        santa.append([*cur])

print(len(santa))

for i in range(0, len(directions), 2):
    print(directions[i], directions[i+1])