# Comprehensions

## Purpose of comprehensions

Comprehensions in Python are concise and powerful constructs for creating new sequences (lists, sets, dictionaries) based on existing sequences. There are three main types of comprehensions:

1. List comprehensions
2. Dictionary Comprehensions
3. Set Comprehensions

Comprehensions offer a concise and readable alternative to traditional loops and `map()`/`filter()` functions. They can also include conditions to further filter the generated elements.

## Examples of Comprehensions

### List Comprehension

List comprehensions create new lists based on existing sequences. Example:

```python
zahlen = [1, 2, 3, 4, 5]
quadrate = [x**2 for x in zahlen]
print(quadrate)  # Ausgabe: [1, 4, 9, 16, 25]
```

This example creates a new list of squares containing the squares of all the numbers from the original list of numbers

### Dictionary Comprehension

Dictionary comprehensions create new dictionaries based on existing sequences. Example:

```python
namen = ["Donald", "Dagobert", "Daisy", "Gustav"]
namenslaengen = {name: len(name) for name in namen}
print(namenslaengen)  # Ausgabe: {'Donald': 6, 'Dagobert': 8, 'Daisy': 5, 'Gustav': 6}
```

This example creates a new dictionary called `name_lengths`, which contains the names as keys and their respective lengths as values

### Set Comprehension

Set comprehensions create new sets based on existing sequences. Example:

```python
zahlen = [1, 2, 2, 3, 3, 4, 5, 5]
quadrate_set = {x**2 for x in zahlen}
print(quadrate_set)  # Ausgabe: {1, 4, 9, 16, 25}
```

This example creates a new set quadrate_se, which contains the unique squares of all the numbers from the original list
numbers

