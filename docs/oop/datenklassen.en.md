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

- The attributes are declared directly in the class.
- Python automatically generates a constructor.
- Printing an object becomes more readable.
- Two objects can be compared based on their attribute values.
