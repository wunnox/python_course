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

Das vollständige Beispiel finden Sie hier:

- [dataclass_person.py](../examples/oop/dataclass_person.py)

## Was zeigt dieses Beispiel?

- Die Attribute werden direkt in der Klasse definiert.
- Python erzeugt automatisch einen Konstruktor.
- Die Ausgabe eines Objekts ist besser lesbar als bei vielen einfachen Standardklassen.
- Zwei Objekte können anhand ihrer Attributwerte verglichen werden.
