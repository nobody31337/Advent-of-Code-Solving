import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/6/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

inst = response.text.split('\n')

partone = [False for _ in range(999*999)]
parttwo = [0 for _ in range(999*999)]

for step in inst[:-1]:
    fx, fy = map(int, step.split()[-3].split(','))
    tx, ty = map(int, step.split()[-1].split(','))

    if step.startswith('turn on'):
        for i in range(fx, tx+1):
            for j in range(fy, ty+1):
                partone[i*999 + j] = True
                parttwo[i*999 + j] = 1
    
    if step.startswith('turn off'):
        for i in range(fx, tx+1):
            for j in range(fy, ty+1):
                partone[i*999 + j] = False
                parttwo[i*999 + j] = 0
    
    if step.startswith('toggle'):
        for i in range(fx, tx+1):
            for j in range(fy, ty+1):
                partone[i*999 + j] = not partone[i*999 + j]
                parttwo[i*999 + j] = 2

print(sum(partone))
print(sum(parttwo))
