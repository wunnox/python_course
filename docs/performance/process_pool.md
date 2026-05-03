# Prozessverarbeitung Pool Processing

Dieses Python-Skript berechnet Primzahlen in einem bestimmten Zahlenbereich unter Verwendung von Multiprocessing mit einem Pool von Arbeitsprozessen. 
Es nutzt das Modul Multiprocessing mit einem Pool, um die Berechnung von Primzahlen auf mehrere Prozesse zu verteilen. Im Vergleich zum reinen Multiprocessing (ohne Pool) bietet dieser Ansatz mehrere Vorteile:
Effiziente Nutzung von Mehrkern-Prozessoren: Der Pool verteilt die Arbeit automatisch auf mehrere Prozesse.
Vereinfachte Verwaltung der Prozesse: Der Pool kümmert sich um das Starten und Beenden der Prozesse.
Verbesserte Skalierbarkeit: Die Anzahl der Prozesse im Pool kann leicht angepasst werden.
Dieser Ansatz kombiniert die Vorteile von Multiprocessing (echte Parallelität) mit einer einfacheren Verwaltung durch den Pool-Mechanismus.


```python
# Module
from time import perf_counter
from multiprocessing import Pool,Pipe

# Variabeln
pc = []            # Liste für Primzahlenzähler
pia, pib = Pipe()  # Pipe für Primzahlen erstellen

# Funktionen
def primrechner(data):
    '''Primzahlen errechnen'''

    print(f"Suche Primzahlen von {data[0]} bis {data[1]}")
    for z in range(data[0], data[1] + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break
    data[2].send(len(pc))
    data[2].close()

def pool_handler():
    p = Pool(3)
    p.map(primrechner, [(1,17000,pia),(17001,24000,pia),(24001,30000,pia)])

if __name__ == "__main__":
    # Prozess starten
    start = perf_counter()
    pool_handler()

    # Abschluss
    anzahlprimzahlen=0

    while pib.poll():
        anzahlprimzahlen = anzahlprimzahlen + pib.recv()

    print("Es wurden", anzahlprimzahlen, "Primzahlen gefunden")
    end = perf_counter()
    print(f"Performance: {round(end - start, 6)} Sec")
```

Download: [process_pool.py](../examples/performance/process_pool.py)

Detaillierte Erklärung:

1. Module und Variablen:
    - Es importiert `perf_counter` aus `time` und `Pool` sowie `Pipe` aus `multiprocessing`.
    - Eine leere Liste `pc` wird für Primzahlen initialisiert.
    - Eine bidirektionale Pipe `pia`, `pib` wird erstellt.
2. Die Funktion `primrechner(data)`:
    - Diese Funktion sucht Primzahlen im Bereich von `data[0]` bis `data[1]`.
    - Der Algorithmus zur Primzahlsuche ist derselbe wie in vorherigen Beispielen.
    - Am Ende sendet sie die Anzahl der gefundenen Primzahlen über die in dataübergebene Pipe.
3. Die Funktion `pool_handler()`:
    - Erstellt einen Pool mit 3 Arbeitsprozessen.
    - Verwendet `p.map()`, um die primrechner-Funktion auf drei verschiedene Datensätze anzuwenden:
        1. (1, 17000, pia)
        2. (17001, 24000, pia)
        3. (24001, 30000, pia)
4. Hauptprogrammablauf:
    - Startet die Zeitmessung.
    - Ruft `pool_handler()` auf, was die Berechnung in mehreren Prozessen startet.
    - Sammelt die Ergebnisse aus der Pipe:
        - Verwendet eine `while`-Schleife mit `pib.poll()`, um zu prüfen, ob Daten verfügbar sind.
        - Summiert die empfangenen Werte zur Gesamtanzahl der Primzahlen.
5. Ergebnisausgabe und Zeitmessung:
    - Gibt die Gesamtanzahl der gefundenen Primzahlen aus.
    - Berechnet und zeigt die Gesamtlaufzeit des Programms an.

Wichtige Anmerkungen:

    - Die Verwendung von `if __name__ == "__main__":` ist wichtig, um Probleme mit rekursiven Aufrufen beim Starten von Multiprozessen zu vermeiden.
    - Die `pc`-Liste ist in diesem Fall prozessspezifisch und wird nicht zwischen den Prozessen geteilt, was Synchronisationsprobleme vermeidet.
    - Die Verwendung von Pipe zur Kommunikation zwischen Prozessen ist effizient, aber in diesem Fall könnte auch der Rückgabewert von `map()` verwendet werden, um die Ergebnisse zu sammeln.  

