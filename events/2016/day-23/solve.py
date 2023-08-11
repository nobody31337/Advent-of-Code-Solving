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

assembunny = response.text.splitlines()

class MatchBreak(Exception): pass

sglarg = ('inc', 'dec', 'tgl')
dblarg = ('jnz', 'cpy')

def run(regs: dict[str, int], steps: list[str]):
    steps = list(map(lambda line: line.split(), steps))
    i = 0
    while i < len(steps):
        offset = 1
        try:
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
                        raise MatchBreak()
                    if steps[i+x][0] in sglarg:
                        steps[i+x][0] = 'dec' if steps[i+x][0] == 'inc' else 'inc'
                    elif steps[i+x][0] in dblarg:
                        steps[i+x][0] = 'cpy' if steps[i+x][0] == 'jnz' else 'jnz'
        except MatchBreak:
            pass
        i += offset


partone = dict(a=7, b=0, c=0, d=0)
parttwo = dict(a=144, b=0, c=0, d=0)

i = 0
while True:
    tmp = dict(a=i, b=0, c=0, d=0)
    run(tmp, assembunny)
    print()

print('Part One: What value should be sent to the safe?')
run(partone, assembunny)
print('The answer:', partone['a'], partone)
print('\nPart Two: Anyway, what value should actually be sent to the safe?')
run(parttwo, assembunny)
print('The answer:', parttwo['a'], parttwo)
