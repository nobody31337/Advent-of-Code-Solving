import requests
import json
from timeit import default_timer as timer
from lib.time_measure import get_time

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/1/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

inst = response.text

start = timer()

partone = 0
parttwo = 0

for i in range(len(inst)):
    partone += 1 if inst[i] == '(' else -1 if inst[i] == ')' else 0
    if parttwo == 0 and partone == -1:
        parttwo = i+1

end = timer() - start

print('Part One: To what floor do the instructions take Santa?')
print('The answer:', partone)

print('\nPart Two: What is the position of the character that causes Santa to first enter the basement?')
print('The answer:', parttwo)

print(f'\nProcess time:', get_time(end))
