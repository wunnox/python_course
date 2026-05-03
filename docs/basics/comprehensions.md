# Comprehensions

## Zweck von Comprehensions

Comprehensions in Python sind kompakte und ausdrucksstarke Konstrukte, um neue Sequenzen (Listen, Sets, Dictionaries) basierend auf existierenden Sequenzen zu erstellen. Es gibt drei Haupttypen von Comprehensions:

1. List Comprehensions
2. Dictionary Comprehensions
3. Set Comprehensions

Comprehensions bieten eine prägnante und lesbare Alternative zu herkömmlichen Schleifen `undmap()/filter()` Funktionen. Sie können auch Bedingungen enthalten, um die erzeugten Elemente weiter zu filtern.

## Beispiele von Comprehensions

### List Comprehension

List Comprehensions erstellen neue Listen basierend auf existierenden Sequenzen.Beispiel:

```python
zahlen = [1, 2, 3, 4, 5]
quadrate = [x**2 for x in zahlen]
print(quadrate)  # Ausgabe: [1, 4, 9, 16, 25]
```

Dieses Beispiel erstellt eine neue Listequadrate, die die Quadrate aller Zahlen aus der ursprünglichen Listezahlenenthält

### Dictionary Comprehension

Dictionary Comprehensions erstellen neue Dictionaries basierend auf existierenden Sequenzen.Beispiel:

```python
namen = ["Donald", "Dagobert", "Daisy", "Gustav"]
namenslaengen = {name: len(name) for name in namen}
print(namenslaengen)  # Ausgabe: {'Donald': 6, 'Dagobert': 8, 'Daisy': 5, 'Gustav': 6}
```

Dieses Beispiel erstellt ein neues Dictionarynamenslaengen, das die Namen als Schlüssel und ihre jeweiligen Längen als Werte enthält

### Set Comprehension

Set Comprehensions erstellen neue Sets basierend auf existierenden Sequenzen.Beispiel:


```python
zahlen = [1, 2, 2, 3, 3, 4, 5, 5]
quadrate_set = {x**2 for x in zahlen}
print(quadrate_set)  # Ausgabe: {1, 4, 9, 16, 25}
```

Dieses Beispiel erstellt ein neues Set quadrate_set, das die eindeutigen Quadrate aller Zahlen aus der ursprünglichen Listezahlenenthält

