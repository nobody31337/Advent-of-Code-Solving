import os

for year in range(2015, 2023):
    for day in range(1, 26):
        path = f'./events/{year}/day-{day:02}'

        # os.makedirs(path)

        # with open(path + '/solve.py', 'a') as f: pass
