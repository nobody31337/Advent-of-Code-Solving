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

data = response.text.splitlines()

graph: dict[dict] = {}

for route in data:
    left, right = route.split(' to ')
    right, dist = right.split(' = ')
    if left not in graph:
        graph[left] = {}
    if right not in graph:
        graph[right] = {}
    
    graph[left][right] = int(dist)
    graph[right][left] = int(dist)

visited = []

def search(loc = None, next_loc = None):
    if loc is None:
        return min(search(x) for x in graph)

    if next_loc is None:
        visited.append(loc)
        ret = min(search(loc, x) for x in graph[loc] if x not in visited)
        visited.remove(loc)
        return ret
    
    return graph[loc][next_loc] + search(next_loc) if len(set(graph[next_loc]) - set(visited)) else 0


print(search())