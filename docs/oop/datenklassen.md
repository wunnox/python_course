# Datenklassen

Datenklassen sind eine vereinfachte Form von Klassen in Python. Sie eignen sich besonders für Klassen, die hauptsächlich Daten in Attributen speichern. Der Dekorator `@dataclass` kann automatisch Methoden wie `__init__()`, `__repr__()` und `__eq__()` erzeugen.

## Einfaches Beispiel

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str
```

## Beispielscript

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

# Create a new instance
person={}
person[123] = Person(name="Anna Müller", age=29, email="anna.mueller@example.com")
person[456] = Person(name="Max Muster", age=32, email="max.muster@example.com")
person[789] = Person(name="Anna Müller", age=29, email="anna.mueller@example.com")

# Access attributes
print(f"Name: {person[123].name}")
print(f"Alter: {person[123].age}")
print(f"Email: {person[123].email}")

# __repr__-Methode shows all the data
print(person[123])

# Check for double entries
if person[123] == person[789]:
    print(f"The records 123 und 789 are identical")
```

Download: [dataclass_person.py](../examples/oop/dataclass_person.py)

- Die Attribute werden direkt in der Klasse definiert.
- Python erzeugt automatisch einen Konstruktor.
- Die Ausgabe eines Objekts ist besser lesbar als bei vielen einfachen Standardklassen.
- Zwei Objekte können anhand ihrer Attributwerte verglichen werden.
