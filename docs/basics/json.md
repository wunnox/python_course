# Json-Dateien verarbeiten

## Json zu Python Datenstrom

```python
import json
jsonData = '{"name": "UM00365", "Nr.CPU": 4}'
pdict = json.loads(jsonData)
print ("#### Json2Python ####")
print (pdict)
print (pdict['name'])
```

Das Skript wandelt einen JSON-formatierten String in ein Python-Dictionary um.
- Ein JSON-formatierter String wird definiert und der Variable jsonData zugewiesen.
- Die Funktion json.loads() wird verwendet, um den JSON-String in ein Python-Objekt umzuwandeln.

## Python zu Json Datenstrom

```python
import json
pdict = {'name': 'UM00365', 'Nr.CPU': 4}
jsonData = json.dumps(pdict)
print ("#### Python2Json ####")
print (jsonData)
```

Das Skript nimmt ein Python-Dictionary und wandelt es in einen JSON-formatierten String um.
Die Funktion `json.dumps()` wird verwendet, um das Python-Dictionary in einen JSON-formatierten String umzuwandeln.
Das Ergebnis wird in der Variable jsonData gespeichert.

## Json in Datei

```python
import json
pdict = {'name': 'UM00365', 'Nr.CPU': 4}
with open('inventar.json', 'w') as outfile:
    json.dump(pdict, outfile)
```

Das Skript nimmt ein Python-Dictionary und speichert es als JSON-formatierte Daten in einer Datei.
Die Funktion `json.dump()` wird verwendet, um das Python-Dictionary `pdict` in die geöffnete Datei zu schreiben.
Das Dictionary wird dabei in das JSON-Format umgewandelt.

## Json von Datei

```python
import json
pdict = json.load(open('inventar.json'))
print ("#### Read Json ####")
print (pdict)
print (pdict['name'])
```

Das Skript liest eine JSON-Datei ('inventar.json') und wandelt ihren Inhalt in ein Python-Dictionary um.
- Die Funktion open('inventar.json') öffnet die Datei 'inventar.json' zum Lesen.
- `json.load()` liest den Inhalt der Datei und wandelt ihn in ein Python-Objekt um.
- Das resultierende Objekt (in diesem Fall ein Dictionary) wird der Variable pdict zugewiesen.
