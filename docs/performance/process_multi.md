# Prozessverarbeitung Multiprozess

## Übersicht Multiprozessing

Das nachfolgende Python-Skript berechnet Primzahlen in einem bestimmten Zahlenbereich unter Verwendung von Multiprocessing. Mit dem Module Multiprocessing wird die Berechnung von Primzahlen auf mehrere Prozesse zu verteilen, was potenziell zu einer schnelleren Ausführung auf Mehrkern-Systemen führen kann. Es demonstriert die Verwendung von Prozessen, Pipes und einfacher Zeitmessung in Python.

```python
# Module
from multiprocessing import Process, Pipe
from time import perf_counter

# Variabeln
pc = []            # Liste für Primzahlenzähler
pia, pib = Pipe()  # Pipe für Primzahlen erstellen

# Funktionen
def primrechner(ps, pe, pia):
    '''Primzahlen errechnen'''

    print(f"Suche Primzahlen von {ps} bis {pe}")
    for z in range(ps, pe + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break
    pia.send(len(pc))
    pia.close()

if __name__ == "__main__":
    start = perf_counter()

    # Prozesse starten
    px = Process(target=primrechner, args=(1, 17000, pia))
    px.start()
    px = Process(target=primrechner, args=(17001, 24000, pia))
    px.start()
    px = Process(target=primrechner, args=(24001, 30000, pia))
    px.start()

    # Abschluss
    anzahlprimzahlen = pib.recv()
    anzahlprimzahlen = anzahlprimzahlen + pib.recv()
    anzahlprimzahlen = anzahlprimzahlen + pib.recv()
    print(f"Es wurden {anzahlprimzahlen} Primzahlen gefunden")
    end = perf_counter()
    print(f"Performance: {round(end - start,6)} Sec")
```

Download: [process_multi.py](../examples/performance/process_multi.py)

Detaillierte Erklärung:

1. Module und Variablen:
    - Es importiert `Process` und `Pipe` aus dem `multiprocessing`-Modul sowie `perf_counter` aus dem `time`-Modul.
    - Es initialisiert eine leere Liste `pc` für Primzahlen und erstellt eine bidirektionale Pipe `pia`, `pib`.
2. Die Funktion `primrechner`:
    - Diese Funktion sucht Primzahlen in einem gegebenen Bereich von `ps` bis `pe`.
    - Sie verwendet einen einfachen Algorithmus zur Primzahlprüfung.
    - Gefundene Primzahlen werden in der Liste `pc` gespeichert.
    - Am Ende sendet sie die Anzahl der gefundenen Primzahlen über die Pipe.
3. Hauptprogramm:
    - Es startet drei separate Prozesse, die jeweils die `primrechner`-Funktion für unterschiedliche Zahlenbereiche ausführen:
        1. 1 bis 17000
        2. 17001 bis 24000
        3. 24001 bis 30000
    - Jeder Prozess verwendet einen eigenen Teil der Pipe zum Senden der Ergebnisse.
4: Ergebnissammlung:
    - Das Hauptprogramm empfängt die Ergebnisse (Anzahl der Primzahlen) von jedem Prozess über die Pipe.
    - Es summiert diese Ergebnisse zur Gesamtanzahl der gefundenen Primzahlen.
5. Leistungsmessung:
    - Es misst die Gesamtlaufzeit des Programms mit `perf_counter()`.
6. Ausgabe:
    - Am Ende gibt das Programm die Gesamtanzahl der gefundenen Primzahlen und die Laufzeit aus.
