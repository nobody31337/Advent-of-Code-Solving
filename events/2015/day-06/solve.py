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

grid = [False for _ in range(999*999)]

for step in inst[:-1]:
    fx, fy = map(int, step.split()[-3].split(','))
    tx, ty = map(int, step.split()[-1].split(','))

    if step.startswith('turn on'):
        for i in range(fx, tx+1):
            for j in range(fy, ty+1):
                grid[i*999 + j] = True
    
    if step.startswith('turn off'):
        for i in range(fx, tx+1):
            for j in range(fy, ty+1):
                grid[i*999 + j] = False
    
    if step.startswith('toggle'):
        for i in range(fx, tx+1):
            for j in range(fy, ty+1):
                grid[i*999 + j] = not grid[i*999 + j]

print(sum(grid))
