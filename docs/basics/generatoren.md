# Generatoren

Generatoren sind spezielle Funktionen, die schrittweise Werte liefern, statt alles auf einmal zu berechnen. Sie merken sich ihren Zustand zwischen den Aufrufen, verbrauchen wenig Speicher und eignen sich ideal für große Datenmengen oder Datenströme, die Sie „on demand“ verarbeiten wollen.

Beispiele von Generatoren

## Typisches Beispiel mit `yield`

```python
def square(n):
    for i in range(n):
        yield i ** 2

for number in square(5):
    print(number)
```

## Generator-Expression (ähnlich wie List Comprehension aber runde Klammern, Lazy)

```python
even_squares = (x**2 for x in range(10) if x % 2 == 0)
print(even_squares) # Zeigt nur Objekt
print(list(even_squares))
```

## Unendlicher Generator

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
