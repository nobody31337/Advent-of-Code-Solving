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

run = digits

for i in range(10):
    digit = run[0]
    ret = ''
    count = 0
    for n in run:
        if digit != n:
            ret += str(count) + digit
            digit = n
            count = 0
        count += 1
    ret += str(count) + digit
    run = ret

print(run)
