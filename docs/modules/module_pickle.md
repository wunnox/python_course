# Modul Pickle

Das Modul `pickle` dient dazu, Python‑Objekte zu serialisieren (in einen Bytestrom zu verwandeln) und später wieder zu deserialisieren, um sie exakt zu rekonstruieren.

Damit kannst du z.B. komplexe Datenstrukturen oder ganze Objektzustände bequem in Dateien speichern (pickle.dump, pickle.load) oder über das Netzwerk übertragen, ohne sie manuell in Textform (JSON, CSV etc.) umwandeln zu müssen.

## Beispiel

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

## Erklärung:

 - daten = {...}: Es wird ein Dictionary mit ein paar Schlüssel‑Wert‑Paaren erstellt.
 - with open("data.pkl", "wb") as f:: Es wird eine Datei im Binärmodus zum Schreiben geöffnet; der with‑Block sorgt dafür, dass sie danach sauber geschlossen wird.
 - pickle.dump(data, f): Das Dictionary wird serialisiert („gepickelt“) und als Bytestrom in diese Datei geschrieben.
 - with open("data.pkl", "rb") as f:: Die Datei wird erneut geöffnet, diesmal im Binärmodus zum Lesen.
 - loaded = pickle.load(f): Die in der Datei gespeicherten Bytes werden deserialisiert („entpickelt“) und wieder in das ursprüngliche Python‑Objekt (hier ein Dictionary) zurückverwandelt.
