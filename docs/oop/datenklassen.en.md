# Data classes

Data classes are a simplified way to define classes in Python. They are especially useful for classes whose main purpose is to store data in attributes. The `@dataclass` decorator can automatically generate methods such as `__init__()`, `__repr__()`, and `__eq__()`.

## Simple example

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str
```

## Example script

The full example is available here:

- [dataclass_person.py](../examples/oop/dataclass_person.py)

## What does this example show?

- The attributes are declared directly in the class.
- Python automatically generates a constructor.
- Printing an object becomes more readable.
- Two objects can be compared based on their attribute values.
