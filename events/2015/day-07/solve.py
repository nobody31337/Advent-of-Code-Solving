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

ops = dict(AND='&', OR='|', RSHIFT='>>', LSHIFT='<<')

def get(wire: str):
    if wire.isnumeric():
        return int(wire)
    
    if wire not in memo:
        match circuit[wire].split():
            case [a]:
                memo[wire] = get(a)
            case ["NOT", a]:
                memo[wire] = ~get(a)
            case [lop, op, rop]:
                exec(f'memo[wire] = {get(lop)} {ops[op]} {get(rop)}')
            case _:
                memo[wire] = 0
        memo[wire] &= 0xffff
        
    return memo[wire]


print('Part One: In little Bobby\'s kit\'s instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?')

partone = get('a')
print('The answer:', partone)

circuit['b'] = str(partone)
memo = {}

print('\nPart Two: What new signal is ultimately provided to wire a?')

parttwo = get('a')
print('The answer:', parttwo)
