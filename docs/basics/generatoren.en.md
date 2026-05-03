# Generators

Generators are special functions that return values incrementally, rather than calculating everything at once. They remember their state between calls, use little memory, and are ideal for large datasets or data streams that you want to process ‘on demand’.

Examples of generators

## Typical example using `yield`

```python
def square(n):
    for i in range(n):
        yield i ** 2

for number in square(5):
    print(number)
```

## Generator expression (similar to list comprehension but with parentheses, lazy)

```python
even_squares = (x**2 for x in range(10) if x % 2 == 0)
print(even_squares) # Only displays the object
print(list(even_squares))
```

## Infinite generator

```python
def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))
```
