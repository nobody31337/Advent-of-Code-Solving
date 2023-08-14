import requests
import json
import re

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/11/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

password = response.text.strip()

def increment(password: list[int]):
    carry = 1
    for i in reversed(range(len(password))):
        if carry == 0:
            break
        
        password[i] += carry
        
        carry = password[i] // 26
        password[i] %= 26
    
    return password


def validate(password):
    # The first requirement
    inc = []
    for letter in password:
        if len(inc) == 3:
            break
        if len(inc) == 0 or inc[-1] + 1 == letter:
            inc.append(letter)
        else:
            inc = []
    
    if len(inc) < 3:
        return False
    
    # The second requirement
    for letter in password:
        if letter in map(ord, 'iol'):
            return False
    
    # The third requirement
    password = ''.join(map(lambda x: chr(x + ord('a')), password))
    if not re.search(r'([a-z])\1[a-z]*([a-z])\2', password):
        return False
    
    return True


def get_next(password):
    password = list(map(lambda x: ord(x) - ord('a'), password))
    while True:
        password = increment(password)

        if validate(password):
            return ''.join(map(lambda x: chr(x + ord('a')), password))


print('Given password:', password)

print('\nPart One: What should his next password be?')

password = get_next(password)

print('The answer:', password)

print('\nPart Two: Santa\'s password expired again. What\'s the next one?')

password = get_next(password)

print('The answer:', password)
