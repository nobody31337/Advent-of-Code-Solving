import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/3/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

directions = response.text

m = {'>': (0, 1), '<': (0, -1), '^': (1, 1), 'v': (1, -1)}

cur = [0, 0]
cur1 = [0, 0]
cur2 = [0, 0]
path = [[*cur]]
path1 = [[*cur1]]

odd_or_even = 0

for d in directions:
    cur[m[d][0]] += m[d][1]

    if odd_or_even == 0:
        cur1[m[d][0]] += m[d][1]
    else:
        cur2[m[d][0]] += m[d][1]
    
    if cur not in path:
        path.append([*cur])
    
    if cur1 not in path1:
        path1.append([*cur1])
    elif cur2 not in path1:
        path1.append([*cur2])

    odd_or_even += 1
    odd_or_even %= 2

print('Part One: How many houses receive at least one present?')
print('The answer:', len(path))

print('\nPart Two: This year, how many houses receive at least one present?')
print('The answer:', len(path1))