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

def search_min(loc = None, next_loc = None):
    if loc is None:
        return min(search_min(x) for x in graph)

    if next_loc is None:
        visited.append(loc)
        ret = min(search_min(loc, x) for x in graph[loc] if x not in visited)
        visited.remove(loc)
        return ret
    
    return graph[loc][next_loc] + (search_min(next_loc) if len(set(graph[next_loc])-set(visited)) else 0)


def search_max(loc = None, next_loc = None):
    if loc is None:
        return max(search_max(x) for x in graph)

    if next_loc is None:
        visited.append(loc)
        ret = max(search_max(loc, x) for x in graph[loc] if x not in visited)
        visited.remove(loc)
        return ret
    
    return graph[loc][next_loc] + (search_max(next_loc) if len(set(graph[next_loc])-set(visited)) else 0)


def search_(loc = None, next_loc = None, length = 0):
    if loc is None:
        for x in graph:
            search_(x)
        return

    if next_loc is None:
        visited.append(loc)
        for x in graph[loc]:
            if x not in visited:
                search_(loc, x, length)
        visited.remove(loc)
        return
    
    length += graph[loc][next_loc]
    if len(set(graph[next_loc])-set(visited)):
        search_(next_loc, length=length)
    elif length == 141 or length == 736:
        print(*visited, next_loc, length)

search_()
print(search_min(), search_max())
print(visited)