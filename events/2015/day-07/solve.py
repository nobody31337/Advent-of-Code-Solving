import requests
import json
from functools import cache
from timeit import default_timer as timer

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/7/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

circuit = dict(map(lambda wire: wire.split(' -> ')[::-1], response.text.splitlines()))

ops = dict(AND='&', OR='|', RSHIFT='>>', LSHIFT='<<')

memo = {}

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

b_backup = circuit['b']

print('Part One: In little Bobby\'s kit\'s instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?')

start = timer()
partone = memo_get('a')
end = timer() - start

print('The answer:', partone)
print(f'Process time: {round(end*1000, 6)} ms')

print('\nPart Two: What new signal is ultimately provided to wire a?')

start = timer()
circuit['b'] = str(partone)
memo = {}

parttwo = memo_get('a')
end = timer() - start

print('The answer:', parttwo)
print(f'Process time: {round(end*1000, 6)} ms')


print('\n\n(Using functools.cache)\n')

circuit['b'] = b_backup

start = timer()
partone = cache_get('a')
end = timer() - start

print('Part One:', partone)
print(f'Process time: {round(end*1000, 6)} ms')

start = timer()
circuit['b'] = str(partone)
cache_get.cache_clear()

parttwo = cache_get('a')
end = timer() - start

print('\nPart Two:', parttwo)
print(f'Process time: {round(end*1000, 6)} ms')
