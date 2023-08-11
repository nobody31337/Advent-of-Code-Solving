import requests
import json
import time

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2016/day/12/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

assembunny = response.text.splitlines()

regs = dict(a=0, b=0, c=0, d=0)

i = 0

while i < len(assembunny):
    offset = 1
    match assembunny[i].split():
        case ['cpy', x, y]:
            regs[y] = regs[x] if x in regs else int(x)
        case ['inc', x]:
            regs[x] += 1
        case ['dec', x]:
            regs[x] -= 1
        case ['jnz', x, y]:
            x = regs[x] if x in regs else int(x)
            y = regs[y] if y in regs else int(y)
            offset = y if x else 1
    i += offset
    print(f'{i:3}', assembunny[i], regs, sep=', ')
    time.sleep(.2)

print(json.dumps(regs, indent=4))
