import requests
import json
from timeit import default_timer as timer

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/8/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

strings = response.text.splitlines()

start = timer()

partone = 0
parttwo = 0

for string in strings:
    lit_len = len(string)
    esc_len = len(eval(string))
    
    partone += lit_len - esc_len
    parttwo += len(string) + string.count('"') + string.count('\\') + 2 - lit_len

end = timer() - start

print('Part One: What is the given data length minus unescaped string data length?')
print(partone)

print('\nPart Two: What is the length of the escaped string of the given data minus given data length?')
print(parttwo)

print(f'\nProcess time: {round(end*1000, 6)} ms')
