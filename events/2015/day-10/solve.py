import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/10/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

digits = response.text.strip()

def look_and_say(inp, time: int = 1):
    if not isinstance(inp, str):
        inp = str(inp)
    
    if time <= 0:
         return inp
    
    digit = inp[0]
    ret = ''
    count = 0
    for n in inp:
        if digit != n:
            ret += str(count) + digit
            digit = n
            count = 0
        count += 1
    ret += str(count) + digit
    return look_and_say(ret, time-1)

print(len(look_and_say(digits, 40)))
