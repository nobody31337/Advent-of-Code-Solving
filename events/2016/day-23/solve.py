import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2016/day/23/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

assembunny = list(map(lambda line: line.split(), response.text.splitlines()))

sglarg = ('inc', 'dec', 'tgl')
dblarg = ('jnz', 'cpy')

def run(regs: dict[str, int], steps: list[list[str]]):
    i = 0
    while i < len(steps):
        offset = 1
        print(' '.join(steps[i]))
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
            case ['tgl', x]:
                x = regs[x] if x in regs else int(x)
                if i + x >= len(steps):
                    continue
                if steps[i+x][0] in sglarg:
                    steps[i+x][0] = 'dec' if steps[i+x][0] == 'inc' else 'inc'
                elif steps[i+x][0] in dblarg:
                    steps[i+x][0] = 'cpy' if steps[i+x][0] == 'jnz' else 'jnz'
        i += offset


partone = dict(a=7, b=0, c=0, d=0)
parttwo = dict(a=0, b=0, c=1, d=0)

print('Part One: What value should be sent to the safe?')
run(partone, assembunny)
print('The answer:', partone['a'])

print('\nPart Two: ')
# run(parttwo, assembunny)
# print('The answer:', parttwo['a'])
