# Pool Processing

This Python script calculates prime numbers within a specified range using multiprocessing with a pool of worker processes.
It utilises the Multiprocessing module with a pool to distribute the calculation of prime numbers across multiple processes. Compared to pure multiprocessing (without a pool), this approach offers several advantages:
Efficient use of multi-core processors: The pool automatically distributes the work across multiple processes.
Simplified process management: The pool handles the starting and stopping of processes.
Improved scalability: The number of processes in the pool can be easily adjusted.
This approach combines the advantages of multiprocessing (true parallelism) with simpler management through the pool mechanism.

```python 
# Modules 
from time import perf_counter
from multiprocessing import Pool, Pipe 

# Variables 
pc = []            # List for prime number counter
pia, pib = Pipe()  # Create a pipe for prime numbers 

# Functions
def primecalc(data):
    '''Calculate prime numbers'''
        
    print(f"Searching for prime numbers from {data[0]} to {data[1]}")
    for z in range(data[0], data[1] + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break
    data[2].send(len(pc))
    data[2].close()

def pool_handler():
    p = Pool(3)
    p.map(primecalc, [(1, 17000, pia), (17001, 24000, pia), (24001, 30000, pia)])
    
if __name__ == "__main__":
    # Start process
    start = perf_counter()
    pool_handler()

    # Completion
    numberofprimes = 0

    while pib.poll():
        numberofprimes = numberofprimes + pib.recv()

    print(f"{numberofprimes} prime numbers found")
    end = perf_counter()
    print(f"Performance: {round(end - start, 6)} sec")
```

Download: [process_pool.py](../examples/performance/process_pool.py)

Detailed explanation:

1. Modules and variables:
    - It imports `perf_counter` from `time` and `Pool`, as well as `Pipe` from `multiprocessing`.
    - An empty list `pc` is initialised for prime numbers.
    - A bidirectional pipe `pia`, `pib` is created.
2. The function `primrechner(data)`:
    - This function searches for prime numbers in the range from `data[0]` to `data[1]`.
    - The algorithm for finding prime numbers is the same as in previous examples.
    - Finally, it sends the number of prime numbers found via the pipe passed in `data`.
3. The function `pool_handler()`:
    - Creates a pool with 3 worker processes.
    - Uses `p.map()` to apply the `primrechner` function to three different data sets:
        1. (1, 17000, pia)
        2. (17001, 24000, pia)
        3. (24001, 30000, pia)
4. Main programme flow:
    - Starts the timer.
    - Calls `pool_handler()`, which starts the calculation across multiple processes.
    - Collects the results from the pipe:
        - Uses a `while` loop with `pib.poll()` to check if data is available.
        - Sums the received values to give the total number of prime numbers.
5. Output and timing:
    - Outputs the total number of prime numbers found.
    - Calculates and displays the total runtime of the programme.
    
Important notes:

    - The use of `if __name__ == "__main__":` is important to avoid problems with recursive calls when launching multiple processes.
    - The `pc` list is process-specific in this case and is not shared between processes, which avoids synchronisation issues.
    - Using a pipe for inter-process communication is efficient, but in this case the return value of `map()` could also be used to collect the results.
