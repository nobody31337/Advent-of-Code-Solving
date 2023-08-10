import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/10/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

digits = list(map(int, response.text.strip()))

print('The input:', ''.join(map(str, digits)))

digits = digits[::-1]

def look_and_say(run, repeat):
    for _ in range(repeat):
        ret = [run[0]]
        count = 0
        for n in run:
            if n != ret[-1]:
                ret += [count, n]
                count = 0
            count += 1
        run = ret + [count]
    return run

print('\nPart One: What is the length of the result after 40 times of the process?')
print('The answer:', len(look_and_say(digits, 40)))

print('\nPart Two: What is the length of the new result after 50 times of the process?')
print('The answer:', len(look_and_say(digits, 50)))
