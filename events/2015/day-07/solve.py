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
    print(f'Getting {x}')
    ret = 0

    if x not in memo:
        match len(x.split()):
            case 1:
                try:
                    ret = int(x)
                except:
                    for gate in circuit:
                        lop, rop = gate.split(' -> ')
                        if rop == x:
                            ret = get(lop)

            case 2:
                ret = ~int(get(x.split()[1])) & 0xffff

            case 3:
                lop, op, rop = x.split()
                match op:
                    case 'AND':
                        ret = get(lop) & get(rop)
                    case 'OR':
                        ret = get(lop) | get(rop)
                    case 'RSHIFT':
                        ret = get(lop) >> get(rop)
                    case 'LSHIFT':
                        ret = get(lop) << get(rop)
            
            case _:
                ret = None
        
        memo[x] = ret
    else:
        ret = memo[x]
    
    print(f'{x} == {ret}')
    
    return ret

print(get('a'))