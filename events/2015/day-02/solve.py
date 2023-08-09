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

total = 0

for size in sizes.split():
    dim = list(map(int,size.split('x')))
    total += dim[0] * dim[1] + dim[1] * dim[2] + dim[0] * dim[2]

print(total * 2)