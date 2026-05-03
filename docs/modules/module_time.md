# Modul Time

Das Modul `time` stellt Funktionen zur Verfügung, um in Python mit Zeitwerten zu arbeiten, etwa aktuelle Zeit auszulesen, Zeitstempel zu konvertieren, Zeitintervalle zu messen und Ausführungen zu pausieren.

> Hinweis:
> Für das berechnen von Zeit- und Datumsangaben eignet sich das Modul `datetime` besser. Aber `time` hat andere ganz nützliche Funktionen

## Beispiele

### time.perf_counter()

`time.perf_counter()` liefert dabei einen hochauflösenden Timer, der sich gut für Performance-Messungen eignet.

```python
import time

def slow():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

start = time.perf_counter()      # Start time
result = slow()                  # Code to be measured
end = time.perf_counter()        # End time

duration = end - start
print(f"Result: {result}")
print(f"Duration: {duration:.4f} Seconds")
```

Download: [time_example.py](../examples/modules/time_example.py)

### time.sleep()

Pausieren eines Skripts um eine bestimmte Zeit, z.B. 0.1 Sekunden

```python
time.sleep(0.1)
```

### time.time()

Ausgabe der Zeit als Unix‑Timestamp in Sekunden seit 1.1.1970.

```python
print(time.time())
```
