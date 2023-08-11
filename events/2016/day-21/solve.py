import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2016/day/21/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

word = list('abcdefgh')

for step in response.text.splitlines():
    match step:
        case ['swap', 'position', x, _, _, y]: # swap position X with position Y
            word[x], word[y] = word[y], word[x]
        case ['swap', 'letter', x, _, _, y]: # swap letter X with letter Y
            pass
        case ['reverse', _, x, _, y]: # reverse positions X through Y
            pass
        case ['rotate', 'based', _, _, _, _, x]: # rotate based on position of letter X
            pass
        case ['rotate', direction, x, _]: # rotate left/right X steps
            pass
        case ['move', 'position', x, _, _, y]: # move position X to position Y
            pass

print(''.join(word))