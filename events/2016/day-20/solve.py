import requests
import json

SMST = 0
BGST = 2 ** 32 - 1

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2016/day/20/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

blacklist: list[tuple[int]] = list(map(lambda x: tuple(map(int, x.decode().split('-'))), response.iter_lines()))

whitelist = []
keyval = {}

for black_ in blacklist:
    isLowBlacked = False
    isHighBlacked = False

    low = black_[0] - 1
    high = black_[1] + 1

    for black in blacklist:
        if low >= black[0] and low <= black[1]:
            isLowBlacked = True
        if high >= black[0] and high <= black[1]:
            isHighBlacked = True
        
        if isLowBlacked and isHighBlacked:
            break
    
    if not isLowBlacked and low >= SMST:
        if low in keyval:
            if keyval[low] == 'low':
                keyval[low] = 'both'
        else:
            keyval[low] = 'high'
    if not isHighBlacked and high <= BGST:
        if high in keyval:
            if keyval[high] == 'high':
                keyval[high] = 'both'
        else:
            keyval[high] = 'low'

keyval = sorted(keyval.items())

for i in range(len(keyval)):
    if i + 1 < len(keyval) and keyval[i][1] == 'low' and keyval[i + 1][1] == 'high':
        whitelist.append((keyval[i][0], keyval[i + 1][0]))
    elif keyval[i][1] == 'both':
        whitelist.append((keyval[i][0], keyval[i][0]))

print('Part One: What is the lowest-valued IP that is not blocked?')
print('The answer:', whitelist[0][0])

print('\nPart Two: How many IPs are allowed by the blacklist?')
print('The answer:', sum(j - i + 1 for i, j in whitelist))
