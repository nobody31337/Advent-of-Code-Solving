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

print(word)

for step in response.text.splitlines():
    match step:
        case ['swap', 'position', a, _, _, b]: # swap position 1 with position 2
            pass
        case ['swap', 'letter', a, _, _, b]: # swap letter a with letter b
            pass
        case ['reverse', _, a, _, b]: # reverse positions 0 through 3
            pass
        case ['rotate', direction, a, _]: # rotate right 2 steps
            pass
