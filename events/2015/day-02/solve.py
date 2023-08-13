import requests
import json
from timeit import default_timer as timer

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/2/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

sizes = response.text.split()

partone = 0
parttwo = 0

tmp = []

start = timer()

for size in sizes:
    dim = list(map(int, size.split('x')))
    partone += 2 * (dim[0] * dim[1] + dim[1] * dim[2] + dim[0] * dim[2])
    tmp = [*dim]
    tmp.remove(max(tmp))
    partone += tmp[0] * tmp[1]
    parttwo += 2 * (tmp[0] + tmp[1]) + dim[0] * dim[1] * dim[2]

end = timer() - start

print('Part One: How many total square feet of wrapping paper should they order?')
print('The answer:', partone)

print('\nPart Two: How many total feet of ribbon should they order?')
print('The answer:', parttwo)

print(f'\nProcess time: {round(end*1000, 6)} ms')
