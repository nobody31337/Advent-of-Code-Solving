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

steps = response.text.splitlines()
partone = 'abcdefgh'
parttwo = 'fbgdceah'

def scramble(password: str, steps):
    password = list(password)
    for step in steps:
        match step.split():
            case ['swap', 'position', x, _, _, y]: # swap position X with position Y
                x = int(x)
                y = int(y)
                password[x], password[y] = password[y], password[x]
            case ['swap', 'letter', x, _, _, y]: # swap letter X with letter Y
                for i in range(len(password)):
                    password[i] = y if password[i] == x else x if password[i] == y else password[i]
            case ['reverse', _, x, _, y]: # reverse positions X through Y
                x = int(x)
                y = int(y) + 1
                password = password[:x] + password[x:y][::-1] + password[y:]
            case ['rotate', 'based', _, _, _, _, x]: # rotate based on position of letter X
                idx = password.index(x)
                shift = (idx + (idx > 3) + 1) % len(password)
                password = password[-shift:] + password[:-shift]
            case ['rotate', direction, x, _]: # rotate left/right X steps
                if direction == 'left':
                    password = password[int(x):] + password[:int(x)]
                else:
                    password = password[-int(x):] + password[:-int(x)]
            case ['move', 'position', x, _, _, y]: # move position X to position Y
                password.insert(int(y), password.pop(int(x)))
    
    return ''.join(password)


def reverse_scramble(password: str, steps):
    password = list(password)
    for step in reversed(steps):
        match step.split():
            case ['swap', 'position', x, _, _, y]: # swap position X with position Y
                x = int(x)
                y = int(y)
                password[x], password[y] = password[y], password[x]
            case ['swap', 'letter', x, _, _, y]: # swap letter X with letter Y
                for i in range(len(password)):
                    password[i] = y if password[i] == x else x if password[i] == y else password[i]
            case ['reverse', _, x, _, y]: # reverse positions X through Y
                x = int(x)
                y = int(y) + 1
                password = password[:x] + password[x:y][::-1] + password[y:]
            case ['rotate', 'based', _, _, _, _, x]: # rotate based on position of letter X
                idx = password.index(x)
                shift = (idx - (1 if idx % 2 else 2)) // 2
                password = password[shift:] + password[:shift]
            case ['rotate', direction, x, _]: # rotate left/right X steps
                if direction == 'left':
                    password = password[-int(x):] + password[:-int(x)]
                else:
                    password = password[int(x):] + password[:int(x)]
            case ['move', 'position', x, _, _, y]: # move position X to position Y
                password.insert(int(x), password.pop(int(y)))
    
    return ''.join(password)


print(scramble(partone, steps))
print(reverse_scramble(parttwo, steps))
