import sys
import subprocess
from timeit import default_timer as timer

def get_time(time: float):
    if time > 1:
        return f'{round(time, 6)} seconds'
    else:
        return f'{round(time * 1000, 6)} ms'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        process = [sys.executable, sys.argv[1]]

        start = timer()
        subprocess.run(process)
        done = timer() - start
        
        print(f'\nElapsed time: {round(done, 6)} seconds')
