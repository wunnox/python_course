# Module Time

The `time` module provides functions for working with time values in Python, such as reading the current time, converting timestamps, measuring time intervals, and pausing execution.

> Note:
> The `datetime` module is better suited for calculating dates and times. However, `time` has other very useful functions

## Examples

### time.perf_counter()

`time.perf_counter()` provides a high-resolution timer that is well suited for performance measurements.

```python
import time

def slow():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

start = time.perf_counter()      # Start time
result = slow()                  # Code to be measured
end = time.perf_counter()        # End time

duration = end - start
print(f"Result: {result}")
print(f"Duration: {duration:.4f} Seconds")
```

Download: [time_example.py](../examples/modules/time_example.py)

### time.sleep()

Pauses a script for a specified duration, e.g. 0.1 seconds

```python
time.sleep(0.1)
```

### time.time()

Outputs the time as a Unix timestamp in seconds since 1 January 1970.

```python
print(time.time())
```
