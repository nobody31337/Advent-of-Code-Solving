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
    ret = 0

    try:
        return int(x)
    except:
        if x not in memo:
            for gate in circuit:
                left, right = gate.split(' -> ')
                if right == x:
                    match len(left.split()):
                        case 1:
                            ret = get(left)

                        case 2:
                            ret = ~int(get(left.split()[1])) & 0xffff

                        case 3:
                            lop, op, rop = left.split()
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
            
            print(f'{x} == {ret}')
            memo[x] = ret
        else:
            ret = memo[x]
    
        return ret

print(get('a'))

a = ''

for i in range(len(circuit)):
    left, right = circuit[i].split(' -> ')
    if right == 'a':
        a = left
        break

for i in range(len(circuit)):
    left, right = circuit[i].split(' -> ')
    if right == 'b':
        circuit[i] = a + ' -> b'
        break

get('a')