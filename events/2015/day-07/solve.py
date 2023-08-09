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

circuit = response.text.split('\n')[:-1]

def get(x: str):
    print(x)
    match len(x.split()):
        case 1:
            try:
                return int(x)
            except:
                for gate in circuit:
                    lop, rop = gate.split(' -> ')
                    if rop == x:
                        return get(lop)

        case 2:
            return ~int(get(x.split()[1])) & 0xffff

        case 3:
            lop, op, rop = x.split()
            match op:
                case 'AND':
                    return get(lop) & get(rop)
                case 'OR':
                    return get(lop) | get(rop)
                case 'RSHIFT':
                    return get(lop) >> get(rop)
                case 'LSHIFT':
                    return get(lop) << get(rop)
        
        case _:
            return None
    

print(get('a'))