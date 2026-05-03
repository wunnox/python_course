# Prozessverarbeitung Concurrent

Dieses Python-Skript berechnet Primzahlen in einem bestimmten Zahlenbereich unter Verwendung von concurrent.futures, einem höheren Abstraktionsniveau für Parallelverarbeitung. Es nutzt fortgeschrittene Konzepte der Parallelverarbeitung in Python, um eine effiziente und skalierbare Lösung für die Primzahlberechnung zu bieten. Es demonstriert die Verwendung von `concurrent.futures`, Chunking und asynchroner Ergebnisverarbeitung, was es zu einem robusten Ansatz für rechenintensive Aufgaben macht.

```python
from concurrent import futures
from time import perf_counter

max_probe = 30000  # Maximum runs
pc=[]              # Liste für Primzahlenzähler

def primrechner(ps,pe):
    '''Primzahlen errechnen'''

    pc=[]
    print(f"Suche Primzahlen von {ps} bis {pe}")
    for z in range(ps,pe+1):
        for z2 in range(2,z):
            if not z%z2: break
        else: pc.append(z)
    return pc

if __name__ == "__main__":
    start = perf_counter()

    with futures.ProcessPoolExecutor(max_workers=3) as e:   ### Max. Anzahl Prozesse
        chunk = 10000                                       ### Chunk Grösse
        fs = {e.submit(primrechner, *(n,n+chunk-1)): n for n in range(1,max_probe,chunk)}
        for f in futures.as_completed(fs):
            pc.extend(f.result())

    # Abschluss
    print(f"Es wurden {len(pc)} Primzahlen gefunden")
    end = perf_counter()
    print(f"Performance: {round(end - start,6)} Sec")
```

Download: [process_concurrent.py](../examples/performance/process_concurrent.py)

Detaillierte Erklärung:

1. Importe und Variablen:
    - Es importiert `futures` aus `concurrent` und `perf_counter` aus `time`.
    - `max_probe` wird auf 30000 gesetzt, was den maximalen zu prüfenden Wert darstellt.
    - Eine leere Liste pc wird initialisiert, um alle gefundenen Primzahlen zu speichern.
2. Die Funktion `primrechner(ps, pe)`:
    - Diese Funktion sucht Primzahlen im Bereich von `ps` (start) bis `pe` (end).
    - Sie verwendet einen effizienteren Algorithmus als die vorherigen Beispiele:
        - Es prüft jede Zahl auf Teilbarkeit durch kleinere Zahlen.
        - Wenn kein Teiler gefunden wird (die else-Klausel der for-Schleife wird erreicht), wird die Zahl als Primzahl zur Liste hinzugefügt.
    - Die Funktion gibt die Liste der gefundenen Primzahlen zurück.
3. Hauptprogrammablauf:
    - Es wird ein `ProcessPoolExecutor` mit maximal 3 Arbeitsprozessen erstellt.
    - Der zu prüfende Zahlenbereich wird in Chunks von 10000 Zahlen aufgeteilt.
    - Für jeden Chunk wird ein separater Auftrag (Task) an den `Executor` übergeben.
    - Die Aufträge werden in einem Dictionary fs gespeichert, wobei der Startwert jedes Chunks als Schlüssel dient.
4. Ergebnissammlung:
    - `futures.as_completed(fs)` wird verwendet, um die Ergebnisse zu sammeln, sobald sie verfügbar sind.
    - Die gefundenen Primzahlen jedes Chunks werden zur Hauptliste `pc` hinzugefügt.
5. Abschluss und Ausgabe:
    - Die Gesamtanzahl der gefundenen Primzahlen wird ausgegeben.
    - Die Gesamtlaufzeit des Programms wird berechnet und angezeigt.

Besonderheiten und Vorteile dieses Ansatzes:
1. Verwendung von `concurrent.futures`:
    - Bietet eine höhere Abstraktionsebene für parallele Ausführung.
    - Vereinfacht die Verwaltung von Prozessen und das Sammeln von Ergebnissen.
2. Chunking:
    - Der Zahlenbereich wird in kleinere Teile (Chunks) aufgeteilt, was eine bessere Lastverteilung ermöglicht.
3. Effizienter Primzahlalgorithmus:
    - Der verwendete Algorithmus ist effizienter als in den anderen Beispielen, da er weniger Operationen pro Zahl durchführt.
4. Flexibilität:
    - Die Anzahl der Arbeitsprozesse und die Chunk-Größe können leicht angepasst werden.
5. Asynchrone Ergebnissammlung:
    - `as_completed()` ermöglicht das Verarbeiten von Ergebnissen, sobald sie verfügbar sind, ohne auf langsamere Prozesse warten zu müssen.

Für weitere Hinweise zum Einsatz des Modules `concurrent` lesen Sie die Seite: 
[concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
