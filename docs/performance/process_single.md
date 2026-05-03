# Prozessverarbeitung Single Prozess

Dieses Python-Skript berechnet Primzahlen in einem bestimmten Zahlenbereich und misst die Ausführungszeit.

```python
from time import perf_counter

pc=[]  # Liste für Primzahlenzähler

def primrechner(ps,pe):
   '''Primzahlen errechnen'''

   print(f"Suche Primzahlen von {ps} bis {pe}")
   for z in range(ps,pe+1):
      pc.append(z)
      for z2 in range(2,z):
         if not z%z2: 
            pc.remove(z)
            break

### Prozess starten
start = perf_counter()
primrechner(1,30000)

### Abschluss
print(f"Es wurden {len(pc)} Primzahlen gefunden")
end = perf_counter()
print(f"Performance: {round(end - start,6)} Sec")
```

Download: [process_single.py](../examples/performance/process_single.py)

Detaillierte Erklärung:

1. Import und Initialisierung:
    - Es importiert `perf_counter` aus dem `time`-Modul zur Zeitmessung.
    - Eine leere Liste `pc` wird initialisiert, um die gefundenen Primzahlen zu speichern.
2. Die Funktion `primrechner(ps, pe)`:
    - Diese Funktion sucht Primzahlen im Bereich von `ps` (start) bis `pe` (end).
    - Sie gibt den Suchbereich aus.
    - Der Algorithmus funktioniert wie folgt:
        - Es durchläuft alle Zahlen im angegebenen Bereich.
        - Jede Zahl wird zunächst der Liste pc hinzugefügt.
        - Dann wird geprüft, ob die Zahl durch eine kleinere Zahl (außer 1) teilbar ist.
        - Wenn eine Teilbarkeit gefunden wird, ist die Zahl keine Primzahl und wird aus pc entfernt.
        - Der break-Befehl beendet die innere Schleife, sobald ein Teiler gefunden wurde.
3. Hauptprogrammablauf:
    - Die Startzeit wird mit `perf_counter()` gemessen.
    - Die primrechner-Funktion wird aufgerufen, um Primzahlen im Bereich von 1 bis 30000 zu finden.
    - Nach Abschluss der Berechnung wird die Anzahl der gefundenen Primzahlen (Länge der Liste pc) ausgegeben.
    - Die Endzeit wird gemessen und die Gesamtlaufzeit berechnet.
4. Ausgabe:
    - Das Programm gibt die Anzahl der gefundenen Primzahlen aus.
    - Es zeigt auch die Laufzeit des Programms in Sekunden an.
