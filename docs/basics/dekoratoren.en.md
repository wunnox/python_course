# Decorators

Decorators are an elegant way to extend functions or classes with additional functionality without modifying the original code.

The key points are:

 - Extending functions without changing the code.
 - Reusable code for logging, caching, validation or timing.
 - Better structure and less code duplication.

## How Decorators Work

Decorators are essentially just nested functions.

```python
def inner_function():
    print("I am the inner_function")

def outer_function():
    print(f"I am the outer_function and run {inner_function}")
    return inner_function

func = outer_function()

func() 
```

A function is called (`outer_function`), which in turn calls another function (`inner_function`).

The `outer_function` is usually called `wrapper`. The name of the `inner_function` is passed to the `wrapper` as an argument.

```python
def func1():
    print("I am function func1")
        
def add_wrapper(fn):
    def wrapper(*args, **kwargs):
        print(f"I am the wrapper and run {fn}")
        return(fn(*args, **kwargs))
    return wrapper

func1 = add_wrapper(func1)

func1()
```

## Sample scripts

### Timing

Measuring the performance of a function

1. The `timer_decorator` measures the time taken to execute the decorated function.
2. The `square` function is a generator that produces the squares of the input numbers.
3. When `square([10,20,30,40])` is called, a generator object is created.
4. The `for` loop iterates over this generator object and outputs each square.

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Runtime of {func.__name__}: {round(end_time - start_time,6)} Seconds")
        return result
    return wrapper

@timer_decorator
def square(n):
   for i in n:
      yield (i*i)

res=square([10,20,30,40])
for number in res:
   print(number)
```
Download: [decorator_time.py](../examples/basics/decorator_time.py)

### Logging

Logging the output of a function

- When `message(‘Max’)` is called, the decorator is activated.
- The decorator executes the `message` function and captures the result.
- The function call is written to the log file along with details.
- The result of the function is returned and displayed.

```python
import logging

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='decorator_test.log'
    )
logger = logging.getLogger('test_logger')

def log_function_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_message=f"Function {func.__name__} called Argument {args}. Result: {result}"
        logger.info(log_message)
        return result
    return wrapper

@log_function_call
def message(name):
    return f"Hello, {name}!"

print(message("Max"))
```

Download: [decorator_logging.py](../examples/basics/decorator_logging.py)

### Cachhing

Speed up calculations using caching

 - The `memoize` decorator creates a cache dictionary for each decorated function.
 - Each time the function is called, it first checks whether the result is already in the cache.
 - If so, the stored result is returned without recalculating the function.
 - If not, the function is executed, the result is stored in the cache and returned.
 - The Fibonacci function uses this memoisation to avoid repeated calculations.

```python
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
```

Download: [decorator_caching.py](../examples/basics/decorator_caching.py)

### Error Handling

Catching errors in a function

- The decorator catches all exceptions that might occur whilst the decorated function is being executed.
- On every call to divide:
    - If the division is successful, the result is returned and printed.
    - If an exception occurs (e.g. division by zero), the error message is printed and 1 is returned.

```python
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in Function {func.__name__}: {str(e)}, return 1")
            return 1
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

for i in (3,0,7):
    print(divide(10, i))
```

Download: [decorator_error_handling.py](../examples/basics/decorator_error_handling.py) 
