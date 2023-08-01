import sys
import subprocess
from timeit import default_timer as timer

if len(sys.argv) > 1:
    process = [sys.executable, sys.argv[1]]

    start = timer()
    subprocess.run(process)
    done = timer() - start
    
    print(f'\nElapsed time: {round(done, 6)} seconds')
