import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/11/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

password = response.text.strip()

def increment(password):
    password = list(map(lambda x: ord(x) - ord('a'), reversed(password)))
    
    carry = 1
    for i in range(len(password)):
        password[i] += carry
        if password[i] < 26:
            carry = 0
        else:
            password[i] %= 26
            carry = 1
    
    return ''.join(map(lambda x: chr(x + ord('a')), reversed(password)))
    
print(password)
for _ in range(100):
    password = increment(password)
    print(password)