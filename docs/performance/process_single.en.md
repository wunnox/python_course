# Single-process processing

This Python script calculates prime numbers within a specified range and measures the execution time.

```python
from time import perf_counter

pc=[]  # List for prime number counter

def primrechner(ps,pe):
   '''Calculate prime numbers'''

   print(f"Searching for prime numbers from {ps} to {pe}")
   for z in range(ps, pe+1):
      pc.append(z)
      for z2 in range(2, z):
         if not z % z2:
            pc.remove(z)
            break

### Start process
start = perf_counter()
primrechner(1, 30000)

### Completion
print(f"{len(pc)} prime numbers were found")
end = perf_counter()
print(f"Performance: {round(end - start, 6)} sec")
```

Download: [process_single.py](../examples/performance/process_single.py)

Detailed explanation:

1. Import and initialisation:
    - It imports `perf_counter` from the `time` module for timing.
    - An empty list `pc` is initialised to store the prime numbers found.
2. The function `primrechner(ps, pe)`:
    - This function searches for prime numbers in the range from `ps` (start) to `pe` (end).
    - It outputs the search range.
    - The algorithm works as follows:
        - It iterates through all numbers in the specified range.
        - Each number is first added to the list pc.
        - It then checks whether the number is divisible by a smaller number (other than 1).
        - If divisibility is found, the number is not a prime number and is removed from pc.
        - The break statement terminates the inner loop as soon as a divisor is found.
3. Main programme flow:
    - The start time is measured using perf_counter().
    - The primrechner function is called to find prime numbers in the range from 1 to 30000.
    - Once the calculation is complete, the number of prime numbers found (length of the list pc) is printed.
    - The end time is measured and the total running time is calculated.
4. Output:
    - The programme prints the number of prime numbers found.
    - It also displays the programme’s running time in seconds.

