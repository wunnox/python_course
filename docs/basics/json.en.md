# Processing JSON files

## JSON to Python data stream

```python
import json
jsonData = “{‘name’: “UM00365”, ‘Nr.CPU’: 4}”
pdict = json.loads(jsonData)
print (‘#### Json2Python ####’)
print (pdict)
print (pdict[“name”])
```

The script converts a JSON-formatted string into a Python dictionary.
- A JSON-formatted string is defined and assigned to the variable jsonData.
- The function json.loads() is used to convert the JSON string into a Python object.

## Python to JSON data stream

```python
import json
pdict = {“name”: “UM00365”, “No.CPU”: 4}
jsonData = json.dumps(pdict)
print (‘#### Python2Json ####’)
print (jsonData)
```

The script takes a Python dictionary and converts it into a JSON-formatted string.
The `json.dumps()` function is used to convert the Python dictionary into a JSON-formatted string.
The result is stored in the variable jsonData.

## JSON to file

```python
import json
pdict = {“name”: “UM00365”, “Nr.CPU”: 4}
with open(“inventory.json”, “w”) as outfile:
    json.dump(pdict, outfile)
```

The script takes a Python dictionary and saves it as JSON-formatted data in a file.
The function `json.dump()` is used to write the Python dictionary `pdict` to the open file.
In doing so, the dictionary is converted into JSON format.

## JSON from a file

```python
import json
pdict = json.load(open(“inventory.json”))
print (‘#### Read JSON ####’)
print (pdict)
print (pdict[“name”])
```

The script reads a JSON file (“inventory.json”) and converts its contents into a Python dictionary.
- The function open(“inventory.json”) opens the file “inventory.json” for reading.
- `json.load()` reads the contents of the file and converts them into a Python object.
- The resulting object (in this case a dictionary) is assigned to the variable pdict.

