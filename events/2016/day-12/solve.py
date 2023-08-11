import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2016/day/12/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

assembunny = response.text.splitlines()

regs = {}

i = 0

while i < len(assembunny):
    offset = 1
    match assembunny[i].split():
        case ['cpy', x, y]:
            regs[y] = int(x) if x.isnumeric() else regs[x]
        case ['inc', x]:
            regs[x] += 1
        case ['dec', x]:
            regs[x] -= 1
        case ['jnz', x, y]:
            x = int(x) if x.isnumeric() else regs[x]
            y = int(y) if y.isnumeric() else regs[y]
            offset = y if x else 1
    i += offset

print(json.dumps(regs, indent=4))