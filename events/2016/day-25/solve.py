import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2016/day/25/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

assembunny = response.text.splitlines()

class MatchBreak(Exception): pass

sglarg = ('inc', 'dec', 'tgl', 'out')
dblarg = ('jnz', 'cpy')

def run(regs: dict[str, int], steps: list[str]):
    steps = list(map(lambda line: line.split(), steps))
    i = 0
    heartbeat = 0
    trace = []
    while 0 <= i < len(steps):
        offset = 1
        try:
            match steps[i]:
                case ['cpy', x, y]:
                    if y in regs:
                        match steps[i+1:i+6]:
                            case [['inc', a], ['dec', _1], ['jnz', _2, '-2'], ['dec', b], ['jnz', b2, '-5']]:
                                if y == _1 == _2 and b == b2:
                                    regs[y] = 0
                                    regs[a] += regs[b] * (regs[x] if x in regs else int(x))
                                    regs[b] = 0
                                    offset = 6
                                    raise MatchBreak
                        regs[y] = regs[x] if x in regs else int(x)
                case ['inc', x]:
                    if x in regs:
                        match steps[i+1:i+3]:
                            case [['dec', y], ['jnz', z, '-2']]:
                                if y == z:
                                    #print('hey!', steps[i:i+3])
                                    regs[x] += regs[y]
                                    regs[y] = 0
                                    offset = 3
                                    raise MatchBreak
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
                        raise MatchBreak()
                    if steps[i+x][0] in sglarg:
                        steps[i+x][0] = 'dec' if steps[i+x][0] == 'inc' else 'inc'
                    elif steps[i+x][0] in dblarg:
                        steps[i+x][0] = 'cpy' if steps[i+x][0] == 'jnz' else 'jnz'
                case ['out', x]:
                    print(regs[x], end=' ')
                    # print(regs[x] if x in regs else x, regs, regs[x] ^ heartbeat)

                    if len(trace) > 0 and not (regs[x] ^ heartbeat):
                            return False
                    heartbeat = regs[x]

                    if regs in trace:
                        return True
                    trace.append(regs.copy())
        except MatchBreak:
            pass
        i += offset

run(dict(a=1, b=0, c=0, d=0), assembunny)