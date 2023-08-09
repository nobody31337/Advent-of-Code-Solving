import requests
import json
import hashlib

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/4/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

content = response.content.strip()

i=0
five = 0
six = 0

while five == 0 or six == 0:
    i+=1
    if five == 0 and hashlib.md5(content + str(i).encode()).hexdigest().startswith('00000'):
        five = i
        print('Starting with 5 zeros:', five)
    if six == 0 and hashlib.md5(content + str(i).encode()).hexdigest().startswith('000000'):
        six = i
        print('Starting with 6 zeros:', six)
