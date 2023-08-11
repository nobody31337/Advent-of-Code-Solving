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
    print(step, word, sep='\n', end='\n\n')
    match step.split():
        case ['swap', 'position', x, _, _, y]: # swap position X with position Y
            x = int(x)
            y = int(y)
            word[x], word[y] = word[y], word[x]
        case ['swap', 'letter', x, _, _, y]: # swap letter X with letter Y
            for i in range(len(word)):
                word[i] = y if word[i] == x else x if word[i] == y else word[i]
        case ['reverse', _, x, _, y]: # reverse positions X through Y
            x = int(x)
            y = int(y) + 1
            word = word[0:x] + word[x:y][::-1] + word[y:]
        case ['rotate', 'based', _, _, _, _, x]: # rotate based on position of letter X
            pass
        case ['rotate', direction, x, _]: # rotate left/right X steps
            pass
        case ['move', 'position', x, _, _, y]: # move position X to position Y
            pass

print(''.join(word))
print(word[0:0])