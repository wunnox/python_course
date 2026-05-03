from time import perf_counter

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# Deactivate the next line to see the difference
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
   
start = perf_counter()
for i in range(40):
    print(fibonacci(i))
end = perf_counter()

print("Runtime:", round(end - start,6), "Sec")
