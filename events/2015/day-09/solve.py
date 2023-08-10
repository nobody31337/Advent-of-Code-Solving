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

partone = 0
parttwo = 0

def search_min_old(loc = None, next_loc = None):
    if loc is None:
        return min(search_min_old(x) for x in graph)

    if next_loc is None:
        visited.append(loc)
        ret = min(search_min_old(loc, x) for x in graph[loc] if x not in visited)
        visited.remove(loc)
        return ret
    
    return graph[loc][next_loc] + (search_min_old(next_loc) if len(set(graph[next_loc])-set(visited)) else 0)


def search_max_old(loc = None, next_loc = None):
    if loc is None:
        return max(search_max_old(x) for x in graph)

    if next_loc is None:
        visited.append(loc)
        ret = max(search_max_old(loc, x) for x in graph[loc] if x not in visited)
        visited.remove(loc)
        return ret
    
    return graph[loc][next_loc] + (search_max_old(next_loc) if len(set(graph[next_loc])-set(visited)) else 0)


def search_min(loc = None):
    if loc is None:
        return min(search_min(x) for x in graph)

    visited.append(loc)
    dist, next_loc = min((graph[loc][x], x) for x in graph[loc] if x not in visited)
    if len(set(graph[next_loc])-set(visited)):
        dist += search_min(next_loc)
    visited.remove(loc)
    return dist


def search_max(loc = None):
    if loc is None:
        return max(search_max(x) for x in graph)

    visited.append(loc)
    dist, next_loc = max((graph[loc][x], x) for x in graph[loc] if x not in visited)
    if len(set(graph[next_loc])-set(visited)):
        dist += search_max(next_loc)
    visited.remove(loc)
    return dist


partone = search_min()
parttwo = search_max()

print('Part One: What is the distance of the shortest route?')
print('The answer:', partone)

print('\nPart Two: What is the distance of the longest route?')
print('The answer:', parttwo)

print('\nJust for fun')

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
    elif length in (partone, parttwo):
        print(*visited, next_loc, length)


search_()
