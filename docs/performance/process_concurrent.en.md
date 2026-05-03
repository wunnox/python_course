# Concurrent Processing

This Python script calculates prime numbers within a specified range using `concurrent.futures`, a higher-level abstraction for parallel processing. It utilises advanced concepts of parallel processing in Python to provide an efficient and scalable solution for prime number calculation. It demonstrates the use of `concurrent.futures`, chunking and asynchronous result processing, making it a robust approach for computationally intensive tasks.

```python
from concurrent import futures
from time import perf_counter

max_probe = 30000  # Maximum runs
pc=[]              # List for prime number counters

def primrechner(ps,pe):
    '''Calculate prime numbers'''

    pc=[]
    print(f"Searching for prime numbers from {ps} to {pe}")
    for z in range(ps,pe+1):
        for z2 in range(2,z):
            if not z%z2: break
        else: pc.append(z)
    return pc

if __name__ == "__main__":
    start = perf_counter()

    with futures.ProcessPoolExecutor(max_workers=3) as e:   ### Maximum number of processes
        chunk = 10000                                       ### Chunk size
        fs = {e.submit(primrechner, *(n, n+chunk-1)): n for n in range(1, max_probe, chunk)}
        for f in futures.as_completed(fs):
            pc.extend(f.result())

    # Conclusion
    print(f"{len(pc)} prime numbers were found")
    end = perf_counter()
    print(f"Performance: {round(end - start,6)} sec")
```

Download: [process_concurrent.py](../examples/performance/process_concurrent.py)

Detailed explanation:
    
1. Imports and variables:
    - It imports `futures` from `concurrent` and `perf_counter` from `time`.
    - `max_probe` is set to 30000, which represents the maximum value to be checked.
    - An empty list `pc` is initialised to store all prime numbers found.
2. The function `primrechner(ps, pe)`:
    - This function searches for prime numbers in the range from `ps` (start) to `pe` (end).
    - It uses a more efficient algorithm than the previous examples:
        - It checks each number for divisibility by smaller numbers.
        - If no divisor is found (the else clause of the for loop is reached), the number is added to the list as a prime number.
    - The function returns the list of prime numbers found.
3. Main programme flow:
    - A `ProcessPoolExecutor` with a maximum of 3 worker processes is created.
    - The range of numbers to be checked is divided into chunks of 10,000 numbers.
    - For each chunk, a separate task is passed to the `Executor`.
    - The tasks are stored in a dictionary fs, with the start value of each chunk serving as the key.
4. Collecting results:
    - `futures.as_completed(fs)` is used to collect the results as soon as they become available.
    - The prime numbers found in each chunk are added to the main list `pc`.
5. Conclusion and Output:
    - The total number of prime numbers found is displayed.
    - The total running time of the programme is calculated and displayed.

Key features and benefits of this approach:
1. Use of `concurrent.futures`:
    - Provides a higher level of abstraction for parallel execution.
    - Simplifies the management of processes and the collection of results.
2. Chunking:
    - The range of numbers is divided into smaller parts (chunks), which enables better load balancing.
3. Efficient prime number algorithm:
    - The algorithm used is more efficient than in the other examples, as it performs fewer operations per number.
4. Flexibility:
    - The number of worker processes and the chunk size can be easily adjusted.
5. Asynchronous result collection:
    - `as_completed()` allows results to be processed as soon as they become available, without having to wait for slower processes.

For further information on using the `concurrent` module, please see the page:
[concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
