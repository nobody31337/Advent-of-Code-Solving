import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/8/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

strings = response.text.splitlines()

partone = 0
parttwo = 0

for string in strings:
    lit_len = len(string)
    esc_len = len(string[1:-1].encode().decode('unicode_escape'))
    partone += lit_len - esc_len
    parttwo += len('"' + string.replace('\\', '\\\\').replace('"', '\\"') + '"') - lit_len

print('Part One: Disregarding the whitespace in the file, '
      + 'what is the number of characters of code for string literals minus '
      + 'the number of characters in memory for the values of the strings in total for the entire file?')
print(partone)
print(parttwo)
