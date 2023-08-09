import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/7/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

circuit = dict(map(lambda wire: wire.split(' -> ')[::-1], response.text.splitlines()))
memo = {}

def get(x: str):
    if x.isnumeric():
        return int(x)
    elif x in memo:
        return memo[x]
    
    match circuit[x].split():
        case [a]:
            memo[x] = get(a)
        case ["NOT", a]:
            memo[x] = ~int(get(a))
        case [lop, op, rop]:
            match op:
                case 'AND':
                    memo[x] = get(lop) & get(rop)
                case 'OR':
                    memo[x] = get(lop) | get(rop)
                case 'RSHIFT':
                    memo[x] = get(lop) >> get(rop)
                case 'LSHIFT':
                    memo[x] = get(lop) << get(rop)
        case _:
            memo[x] = 0
    memo[x] = memo[x] & 0xffff

    return memo[x]


print('Part One: In little Bobby\'s kit\'s instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?')

partone = get('a')
print('The answer:', partone)

circuit['b'] = str(partone)
memo = {}

print('\nPart Two: What new signal is ultimately provided to wire a?')

parttwo = get('a')
print('The answer:', parttwo)
