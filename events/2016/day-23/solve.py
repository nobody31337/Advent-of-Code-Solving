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

sglarg = ('inc', 'dec', 'tgl')
dblarg = ('jnz', 'cpy')

def run(regs: dict[str, int], steps: list[str]):
    steps = list(map(lambda line: line.split(), steps))
    i = 0
    while 0 <= i < len(steps):
        offset = 1
        
        match steps[i]:
            case ['cpy', x, y]:
                if y in regs:
                    match steps[i+1:i+6]:
                        case [['inc', a], ['dec', y1], ['jnz', y2, '-2'], ['dec', b], ['jnz', b2, '-5']]:
                            if y == y1 == y2 and b == b2:
                                regs[y] = 0
                                regs[a] += regs[b] * (regs[x] if x in regs else int(x))
                                regs[b] = 0
                                i += 6
                                continue
                    regs[y] = regs[x] if x in regs else int(x)
            case ['inc', x]:
                if x in regs:
                    match steps[i+1:i+3]:
                        case [['dec', a], ['jnz', a1, '-2']]:
                            if a == a1:
                                regs[x] += regs[a]
                                regs[a] = 0
                                i += 3
                                continue
                    regs[x] += 1
            case ['dec', x]:
                if x in regs:
                    regs[x] -= 1
            case ['jnz', x, y]:
                x = regs[x] if x in regs else int(x)
                y = regs[y] if y in regs else int(y)
                offset = y if x else 1
            case ['tgl', x]:
                x = regs[x] if x in regs else int(x)
                if i + x >= len(steps) or i + x < 0:
                    i += 1
                    continue
                if steps[i+x][0] in sglarg:
                    steps[i+x][0] = 'dec' if steps[i+x][0] == 'inc' else 'inc'
                elif steps[i+x][0] in dblarg:
                    steps[i+x][0] = 'cpy' if steps[i+x][0] == 'jnz' else 'jnz'

        i += offset


partone = dict(a=7, b=0, c=0, d=0)
parttwo = dict(a=12, b=0, c=0, d=0)

print('Part One: What value should be sent to the safe?')
run(partone, assembunny)
print('The answer:', partone['a'])
print('\nPart Two: Anyway, what value should actually be sent to the safe?')
run(parttwo, assembunny)
print('The answer:', parttwo['a'])

print('\nJust for fun:')

for i in range(21):
    print(f'{i:2}: {run(dict(a=i, b=0, c=0, d=0), assembunny)}')