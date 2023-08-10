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

digits = list(map(int, response.text.strip()))

print(''.join(digits))

run = digits[::-1]

def look_and_say(repeat):
    for _ in range(repeat):
        ret = [run[0]]
        count = 0
        for n in run:
            if ret[-1] != n:
                ret += [count, n]
                count = 0
            count += 1
        run = ret + [count]
    return run

print(len(run))
