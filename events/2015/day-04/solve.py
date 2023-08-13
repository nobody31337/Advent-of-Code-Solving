import requests
import json
import hashlib
from timeit import default_timer as timer

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/4/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

content = response.content.strip()

print('Given key:', content.decode())

i = 0

five = 0
six = 0

start = timer()

while five == 0 or six == 0:
    i += 1
    if five == 0 and hashlib.md5(content + str(i).encode()).hexdigest().startswith('00000'):
        five = i
        print('\nPart One, starting with 5 zeros:', five)
        print(f'Timestamp: {round(timer() - start, 6)} seconds')
    if six == 0 and hashlib.md5(content + str(i).encode()).hexdigest().startswith('000000'):
        six = i
        print('\nPart Two, starting with 6 zeros:', six)
        print(f'Timestamp: {round(timer() - start, 6)} seconds')
