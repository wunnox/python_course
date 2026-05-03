# Module Pickle

The `pickle` module is used to serialise Python objects (convert them into a byte stream) and later deserialise them to reconstruct them exactly.

This allows you, for example, to conveniently save complex data structures or entire object states to files (pickle.dump, pickle.load) or transfer them over a network without having to manually convert them into text format (JSON, CSV, etc.).

## Example

```python
import pickle

data = {"name": "Peter", "course": "Python", "participant": 12}

# Save (dump)
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Laden (load)
with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)

print(loaded)
```

Download: [pickle_example.py](../examples/modules/pickle_example.py)


## Explanation:

 - data = {...}: A dictionary containing a few key-value pairs is created.
 - with open(‘data.pkl’, ‘wb’) as f:: A file is opened in binary mode for writing; the `with` block ensures that it is closed properly afterwards.
 - pickle.dump(data, f): The dictionary is serialised (“pickled”) and written to this file as a byte stream.
 - with open(‘data.pkl’, ‘rb’) as f:: The file is opened again, this time in binary mode for reading.
 - loaded = pickle.load(f): The bytes stored in the file are deserialised (“unpickled”) and converted back into the original Python object (in this case, a dictionary).
