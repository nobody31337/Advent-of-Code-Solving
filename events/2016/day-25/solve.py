import requests
import json
from timeit import default_timer as timer

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2016/day/25/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

assembunny = response.text.splitlines()

sglarg = ('inc', 'dec', 'tgl', 'out')
dblarg = ('jnz', 'cpy')

def run(regs: dict[str, int], steps: list[str]):
    steps = list(map(lambda line: line.split(), steps))
    i = 0
    recent = None
    trace = []

    while 0 <= i < len(steps):
        offset = 1

        match steps[i]:
            case ['cpy', x, y]:
                if y in regs:
                    # Long steps short: multiply ------
                    #          : do {
                    # cpy x y  :     y = x;
                    #          :     do {
                    # inc a    :         a += 1;
                    # dec y    :         y -= 1;
                    # jnz y -2 :     } while (y != 0);
                    # dec b    :     b -= 1;
                    # jnz b -5 : } while (b != 0);
                    #
                    # Simple logic ->
                    # a += b * x;
                    # y = 0;
                    # b = 0;
                    match steps[i+1:i+6]:
                        case [['inc', a], ['dec', y1], ['jnz', y2, '-2'], ['dec', b], ['jnz', b2, '-5']]:
                            if y == y1 == y2 and b == b2:
                                regs[a] += regs[b] * (regs[x] if x in regs else int(x))
                                regs[y] = 0
                                regs[b] = 0
                                i += 6
                                continue
                    # ---------------------------------
                    regs[y] = regs[x] if x in regs else int(x)
            case ['inc', x]:
                if x in regs:
                    # Long steps short: summation -----
                    #          : do {
                    # inc x    :     x += 1;
                    # dec a    :     a -= 1;
                    # jnz a -2 : } while(a != 0);
                    #
                    # Simple logic ->
                    # x += a
                    # a = 0
                    match steps[i+1:i+3]:
                        case [['dec', a], ['jnz', a1, '-2']]:
                            if a == a1:
                                regs[x] += regs[a]
                                regs[a] = 0
                                i += 3
                                continue
                    # ---------------------------------
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
            case ['out', x]:
                output = regs[x] if x in regs else int(x)
                
                if output == recent:
                    return False
                recent = output

                if regs in trace:
                    return True
                trace.append(regs.copy())

        i += offset


print('Part One: What is the lowest positive integer that can be used?')

start = timer()

partone = 0
while not run(dict(a=partone, b=0, c=0, d=0), assembunny):
    partone += 1

end = timer() - start

print('The answer:', partone)

print(f'Process time: {round(end, 6)} seconds')
