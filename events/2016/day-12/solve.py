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

assembunny = list(map(lambda line: line.split(), response.text.splitlines()))

def run(regs: dict[str, int], steps: list[list[str]]):
    i = 0
    while i < len(steps):
        offset = 1
        match steps[i]:
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


partone = dict(a=0, b=0, c=0, d=0)
parttwo = dict(a=0, b=0, c=1, d=0)

print('Part One: After executing the assembunny code in your puzzle input, what value is left in register a?')
run(partone, assembunny)
print('The answer:', partone['a'])

print('\nPart Two: If you instead initialize register c to be 1, what value is now left in register a?')
run(parttwo, assembunny)
print('The answer:', parttwo['a'])
