import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/1/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

inst = response.text

print('Part One: To what floor do the instructions take Santa?')
print('The answer:', inst.count('(') - inst.count(')'))

print('Part Two: What is the position of the character that causes Santa to first enter the basement?')
for i in range(len(inst)):
    if inst[:i+1].count('(') - inst[:i+1].count(')') == -1:
        print('The answer:', i+1)
        break