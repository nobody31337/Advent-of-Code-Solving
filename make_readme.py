import os
import json
import requests
from bs4 import BeautifulSoup

with open('data.json', 'r') as js:
    data = json.load(js)

cookies = data['cookies']

solvepy_template = '''import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/{}/day/{}/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)'''

for year in range(2015, 2023):
    for day in range(1, 26):
        path = f'./events/{year}/day-{day:02}'

        url = f'https://adventofcode.com/{year}/day/{day}'

        response = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.main.find_all('article')

        '''
        with open(path + '/solve.py', 'w') as solvepy:
            solvepy.write(solvepy_template.format(year, day))

        with open(path + '/README.md', 'w') as readme:
            readme.write(f'# Solving [{year} day {day:02}]({url})\n')
        
        with open(path + '/backup/input.txt', 'wb') as inp_text:
            response = requests.get(url + '/input', cookies=cookies)
            inp_text.write(response.content)
        '''

        if not os.path.exists(path + '/backup'):
            os.mkdir(path + '/backup')

        with open(path + '/backup/README.md', 'w') as readme:
            readme.write(f'# The Advent of Code on [{year} day {day:02}]({url})')

            for article in articles:
                for content in article.contents:
                    text = content.text.strip().replace('\xa0', ' ').replace('\n', '\\\n')
                    if len(text) > 0:
                        readme.write('\n\n' + text)
    
        print(f'{year} day {day:02} done')
