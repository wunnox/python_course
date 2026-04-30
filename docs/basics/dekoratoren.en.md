# Decorators

Decorators in Python serve several important purposes:

1. Extending functionality:
   - They allow you to extend the core functionality of a function without modifying the original code.
   - Useful for adding features such as logging, timing or error handling.
2. Code reuse:
   - Decorators promote code reuse by extracting common functionality into separate functions.
3. Separation of concerns:
   - They help to separate the main code from additional functions such as validation or caching.
4. Aspect-oriented programming:
   - Enable the implementation of aspect-oriented programming in Python.

Decorators thus offer an elegant and powerful way to extend and modify the behaviour of functions and classes in Python.

## Sample script

Here are a few examples of decorators:

- [decorator_time.py](../examples/basics/decorator_time.py) -> Measures the execution time of a script
- [decorator_logging.py](../examples/basics/decorator_logging.py) -> Logs all output from a script
- [decorator_caching.py](../examples/basics/decorator_caching.py) -> Speeds up the execution time of a script
- [decorator_error_handling.py](../examples/basics/decorator_error_handling.py) -> Catches errors in a script

### What does decorator_time.py do?
1. The timer_decorator measures the time taken to execute the decorated function.
2. The `quadrat` function is a generator that produces the squares of the input numbers.
3. When `quadrat([10,20,30,40])` is called, a generator object is created.
4. The `for` loop iterates over this generator object and outputs each square.

### What does decorator_logging.py do?

1. When message(‘Max’) is called, the decorator is activated.
2. The decorator executes the message function and captures the result.
3. The function call is written to the log file along with details.
4. The result of the function is returned and printed.

### What does decorator_caching.py do?

1. The memoize decorator creates a cache dictionary for each decorated function.
2. Each time the function is called, it first checks whether the result is already in the cache.
3. If so, the stored result is returned without recalculating the function.
4. If not, the function is executed, the result is stored in the cache and returned.
5. The Fibonacci function uses this memoisation to avoid repeated calculations.

### What does decorator_error_handling.py do

1. The decorator catches all exceptions that might occur during the execution of the decorated function.
2. On every call to divide:
   - If the division is successful, the result is returned and printed.
   - If an exception occurs (e.g. division by zero), the error message is printed and 1 is returned.
