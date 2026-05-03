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

