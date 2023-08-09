import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2016/day/20/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

SMST = 0
BGST = 2 ** 32 - 1

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
            if keyval[low] == 'left':
                keyval[low] = 'both'
        else:
            keyval[low] = 'right'
    if not isHighBlacked and high <= BGST:
        if high in keyval:
            if keyval[high] == 'right':
                keyval[high] = 'both'
        else:
            keyval[high] = 'left'

keyval = sorted(keyval.items())

for i in range(len(keyval)):
    if i + 1 < len(keyval) and keyval[i][1] == 'left' and keyval[i + 1][1] == 'right':
        whitelist.append((keyval[i][0], keyval[i + 1][0]))
    elif keyval[i][1] == 'both':
        whitelist.append((keyval[i][0], keyval[i][0]))

print('Part One: What is the lowest-valued IP that is not blocked?')
print('The answer:', whitelist[0][0])

print('\nPart Two: How many IPs are allowed by the blacklist?')
print('The answer:', sum(j - i + 1 for i, j in whitelist))

'''
def int_to_ip(ip: int):
    ip1 = ip >> 24
    ip2 = (ip >> 16) % 256
    ip3 = (ip >> 8) % 256
    ip4 = ip % 256
    
    return f'{ip1}.{ip2}.{ip3}.{ip4}'


print('\n\nI\'m just gonna print all the IPs in the whitelist for fun.\n')
for whited_range in whitelist:
    for ip in range(whited_range[0], whited_range[1] + 1):
        print(int_to_ip(ip))
'''
