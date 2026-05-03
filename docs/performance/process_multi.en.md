# Multi-process processing

## Overview of multi-processing

The following Python script calculates prime numbers within a specified range using multiprocessing. The multiprocessing module allows the calculation of prime numbers to be distributed across multiple processes, which can potentially lead to faster execution on multi-core systems. It demonstrates the use of processes, pipes and simple timing in Python.

```python
# Modules
from multiprocessing import Process, Pipe
from time import perf_counter

# Variables
pc = []            # List for prime number counter
pia, pib = Pipe()  # Create pipe for prime numbers

# Functions
def primecalc(ps, pe, pia):
    '''Calculate prime numbers'''

    print(f"Searching for prime numbers from {ps} to {pe}")
    for z in range(ps, pe + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break
    pia.send(len(pc))
    pia.close()

if __name__ == "__main__":
    start = perf_counter()

    # Start processes
    px = Process(target=primecalc, args=(1, 17000, pia))
    px.start()
    px = Process(target=primecalc, args=(17001, 24000, pia))
    px.start()
    px = Process(target=primecalc, args=(24001, 30000, pia))
    px.start()

    # Completion
    numberofprimes = pib.recv()
    numberofprimes = numberofprimes + pib.recv()
    numberofprimes = numberofprimes + pib.recv()

    print(f"{numberofprimes} prime numbers found")
    end = perf_counter()
    print(f"Performance: {round(end - start, 6)} sec")
```

Download: [process_multi.py](../examples/performance/process_multi.py)

Detailed explanation:

1. Modules and variables:
    - It imports `Process` and `Pipe` from the `multiprocessing` module, as well as `perf_counter` from the time module.
    - It initialises an empty list `pc` for prime numbers and creates a bidirectional pipe `pia`, `pib`.
2. The primrechner function:
    - This function searches for prime numbers in a given range from `ps` to `pe`.
    - It uses a simple algorithm for prime number testing.
    - Prime numbers found are stored in the list `pc`.
    - Finally, it sends the number of prime numbers found via the pipe.
3. Main programme:
    - It launches three separate processes, each of which executes the `primecalc` function for different ranges of numbers:
        1. 1 to 17,000
        2. 17,001 to 24,000
        3. 24,001 to 30,000
    - Each process uses its own section of the pipe to send the results.
4: Collecting results:
    - The main programme receives the results (number of prime numbers) from each process via the pipe.
    - It sums these results to give the total number of prime numbers found.
5. Performance measurement:
    - It measures the total runtime of the programme using `perf_counter()`.
6. Output:
    - At the end, the programme outputs the total number of prime numbers found and the runtime.
