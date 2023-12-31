import requests
import json
from timeit import default_timer as timer

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/6/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

inst = response.text.splitlines()

start = timer()

partone = [False for _ in range(999*999)]
parttwo = [0 for _ in range(999*999)]

for step in inst[:-1]:
    fx, fy = map(int, step.split()[-3].split(','))
    tx, ty = map(int, step.split()[-1].split(','))

    if step.startswith('turn on'):
        for i in range(fx, tx+1):
            for j in range(fy, ty+1):
                partone[i*999 + j] = True
                parttwo[i*999 + j] += 1
    
    if step.startswith('turn off'):
        for i in range(fx, tx+1):
            for j in range(fy, ty+1):
                partone[i*999 + j] = False
                if parttwo[i*999 + j] > 0: parttwo[i*999 + j] -= 1
    
    if step.startswith('toggle'):
        for i in range(fx, tx+1):
            for j in range(fy, ty+1):
                partone[i*999 + j] = not partone[i*999 + j]
                parttwo[i*999 + j] += 2

end = timer() - start

print('Part One: After following the instructions, how many lights are lit?')
print('The answer:', sum(partone))

print('\nPart Two: What is the total brightness of all lights combined after following Santa\'s instructions?')
print('The answer:', sum(parttwo))

print(f'\nProcess time: {round(end, 6)} seconds')