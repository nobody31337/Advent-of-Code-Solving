import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/2/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

sizes = response.text

partone = 0
parttwo = 0

for size in sizes.split():
    dim = list(map(int, size.split('x')))
    partone += 2 * (dim[0] * dim[1] + dim[1] * dim[2] + dim[0] * dim[2])
    dim.remove(max(dim))
    partone += dim[0] * dim[1]
    parttwo += 2 * (dim[0] + dim[1])


print(partone)
print(parttwo)