# Iterators

Iterators return elements of a sequence one at a time and only when needed, whilst keeping track of their current position. This allows you to efficiently iterate over any data structures (lists, files, streams, infinite sequences) using `for` loops without having to keep all values in memory at once.

## Examples of iterators

### Using `iter`

```python
fruits = [‘apple’, “banana”, ‘pineapple’]
my_iterator = iter(fruits)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
```

### Using enumerate

```python
fruits = [‘apple’, “banana”, ‘pineapple’]
for index, fruit in enumerate(fruits):
    print(f‘{index}: {fruit}’)
```

### Using zip

```python
ind = [0, 1, 2]
obj = [‘Apple’, “Banana”, ‘Pineapple’]

for index, object in zip(ind, obj):
    print(f‘{index} : {object}’)
```

### Using yield

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))
```

### Using itertools

```python
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

for item in chain(list1, list2, list3):
    print(item)
```

### Object-oriented

```python
class EvenNumbers:
    def __init__(self, max_value):
        self.max = max_value
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= self.max:
            result = self.number
            self.number += 2
            return result
        else:
            raise StopIteration

even = EvenNumbers(10)

print(next(even))
print(next(even))
print(next(even))

# or

for num in even:
    print(num)
```

`__iter__` makes the object ‘iterable’, `__next__` defines what is returned in the next step and when it ends (StopIteration).

## Practical examples

### Efficient data access with large data sets

Uses little memory, even with large files

```python
def large_file_reader(file):
    with open(file, “r”) as file:
        for line in file:
            yield line.strip()

for line in large_file_reader(“/var/logs/keybagd.log.1”):
    print(line)
```

