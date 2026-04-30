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
