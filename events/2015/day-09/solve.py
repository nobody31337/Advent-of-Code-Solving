import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/9/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

graph = response.text.splitlines()

dijkstra: dict[dict] = {}

for route in graph:
    left, right = route.split(' to ')
    right, dist = right.split(' = ')
    if left not in dijkstra:
        dijkstra[left] = {}
    if right not in dijkstra:
        dijkstra[right] = {}
    
    dijkstra[left][right] = int(dist)
    dijkstra[right][left] = int(dist)

print(dijkstra)