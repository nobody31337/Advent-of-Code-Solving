import requests
import json
import time

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/7/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

circuit = response.text.split('\n')[:-1]
memo = {}

def get(x: str):
    try:
        return int(x)
    except:
        if x not in memo:
            for gate in circuit:
                left, right = gate.split(' -> ')
                if right == x:
                    match len(left.split()):
                        case 1:
                            memo[x] = get(left)

                        case 2:
                            memo[x] = ~int(get(left.split()[1])) & 0xffff

                        case 3:
                            lop, op, rop = left.split()
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
                            memo[x] = None
    
        return memo[x]

partone = get('a')

for i in range(len(circuit)):
    left, right = circuit[i].split(' -> ')
    if right == 'b':
        circuit[i] = '3176 -> b'
        break

memo = {}

parttwo = get('a')

print('Part One: In little Bobby\'s kit\'s instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?')
print('The answer:', partone)

print('\nPart Two: What new signal is ultimately provided to wire a?')
print('The answer:', parttwo)
