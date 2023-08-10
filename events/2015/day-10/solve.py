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

run = digits[::-1]

for i in range(50):
    ret = run[0]
    count = 0
    for n in run:
        if ret[-1] != n:
            ret += str(count) + n
            count = 0
        count += 1
    ret += str(count)
    run = ret

print(len(run))
