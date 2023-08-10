import requests
import json
import re

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/5/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

words = response.text.split()

vowels = 'aeiou'

partone = 0
parttwo = 0

for word in words:
    if sum(word.count(v) for v in vowels) > 2 and re.search(r'([a-z])\1', word) and not ('ab' in word or 'cd' in word or 'pq' in word or 'xy' in word):
        partone += 1
    if re.search(r'([a-z]{2})[a-z]*\1', word) and re.search(r'([a-z])[a-z]\1', word):
        parttwo += 1

print('Nice words part 1:', partone)
print('Nice words part 2:', parttwo)
