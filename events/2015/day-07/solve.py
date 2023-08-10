import requests
import json
from functools import cache

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

def memo_get(wire: str):
    if wire.isnumeric():
        return int(wire)
    
    if wire not in memo:
        match circuit[wire].split():
            case [a]:
                memo[wire] = memo_get(a)
            case ["NOT", a]:
                memo[wire] = ~memo_get(a)
            case [lop, op, rop]:
                memo[wire] = eval(f'{memo_get(lop)} {ops[op]} {memo_get(rop)}')
            case _:
                memo[wire] = 0
        memo[wire] &= 0xffff
        
    return memo[wire]

@cache
def cache_get(wire: str):
    if wire.isnumeric():
        return int(wire)
    
    match circuit[wire].split():
        case [a]:
            return cache_get(a)
        case ["NOT", a]:
            return ~cache_get(a) & 0xffff
        case [lop, op, rop]:
            return eval(f'{cache_get(lop)} {ops[op]} {cache_get(rop)}') & 0xffff


print('\n(Using memoization)\n')

print('Part One: In little Bobby\'s kit\'s instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?')

partone = memo_get('a')
print('The answer:', partone)

b_backup = circuit['b']
circuit['b'] = str(partone)
memo = {}

print('\nPart Two: What new signal is ultimately provided to wire a?')

parttwo = memo_get('a')
print('The answer:', parttwo)


print('\n\n(Using functools.cache)\n')

print('Part One: In little Bobby\'s kit\'s instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?')

circuit['b'] = b_backup

partone = cache_get('a')
print('The answer:', partone)

circuit['b'] = str(partone)
cache_get.cache_clear()

print('\nPart Two: What new signal is ultimately provided to wire a?')

parttwo = cache_get('a')
print('The answer:', parttwo)
