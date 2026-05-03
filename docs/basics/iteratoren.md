# Iteratoren

Iteratoren liefern Elemente einer Sequenz schrittweise und nur bei Bedarf und merken sich dabei ihre aktuelle Position. So kannst du beliebige Datenstrukturen (Listen, Dateien, Streams, unendliche Sequenzen) effizient mit `for`-Schleifen durchlaufen, ohne alle Werte gleichzeitig im Speicher zu halten.

## Beispiele von Iteratoren

### Mit iter

```python
fruechte = ["Apfel", "Banane", "Ananas"]
mein_iterator = iter(fruechte)

print(next(mein_iterator))
print(next(mein_iterator))
print(next(mein_iterator))
```

### Mit enumerate

```python
fruechte = ["Apfel", "Banane", "Ananas"]
for index, frucht in enumerate(fruechte):
    print(f"{index}: {frucht}")
```

### Mit zip

```python
ind = [0, 1, 2]
obj = ["Apfel", "Banane", "Ananas"]

for index, objekt in zip(ind, obj):
    print(f"{index} : {objekt}")
```

### Mit yield

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

### Mit itertools

```python
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

for item in chain(list1, list2, list3):
    print(item)
```

### Objekt Orientiert

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

# oder

for num in even:
    print(num)
```

`__iter__` macht das Objekt „iterierbar“, `__next__` definiert, was beim nächsten Schritt zurückgegeben wird und wann Schluss ist (StopIteration).

## Praktische Beispiele

### Effizienter Datenzugriff mit großen Datenmengen

Verwendet wenig Speicher, selbst bei großen Dateien

```python
def large_file_reader(datei):
    with open(datei, 'r') as file:
        for zeile in file:
            yield zeile.strip()

for zeile in large_file_reader('/var/logs/keybagd.log.1'):
    print(zeile)
```

