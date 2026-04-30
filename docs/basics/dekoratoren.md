# Dekoratoren

Dekoratoren in Python dienen mehreren wichtigen Zwecken:

1. Erweiterung der Funktionalität:
   - Sie ermöglichen es, die Kernfunktionalität einer Funktion zu erweitern, ohne den ursprünglichen Code zu ändern.
   - Nützlich für das Hinzufügen von Funktionen wie Logging, Timing oder Fehlerbehandlung.
2. Code-Wiederverwendung:
   - Dekoratoren fördern die Wiederverwendung von Code, indem sie gemeinsame Funktionalitäten in separate Funktionen auslagern.
3. Trennung von Belangen:
   - Sie helfen, den Hauptcode von zusätzlichen Funktionen wie Validierung oder Caching zu trennen.
4. Aspektorientierte Programmierung:
   - Ermöglichen die Implementierung von aspektorientierter Programmierung in Python.

Dekoratoren bieten somit eine elegante und leistungsfähige Möglichkeit, das Verhalten von Funktionen und Klassen in Python zu erweitern und zu modifizieren.

## Beispielscripts

Nachfolgende einige Beispiele für Dekoratoren;

- [decorator_time.py](../examples/basics/decorator_time.py) -> Misst die Laufzeit eines Scripts
- [decorator_logging.py](../examples/basics/decorator_logging.py) -> Loggt alle Ausgaben eines Scripts
- [decorator_caching.py](../examples/basics/decorator_caching.py) -> Beschleunigt die Laufzeit eines Scripts
- [decorator_error_handling.py](../examples/basics/decorator_error_handling.py) -> Fängt Fehler in einem Script ab

### Was macht decorator_time.py

1. Der timer_decorator misst die Zeit, die für die Ausführung der dekorierten Funktion benötigt wird.
2. Die quadrat-Funktion ist ein Generator, der Quadrate der Eingabezahlen erzeugt.
3. Beim Aufruf von quadrat([10,20,30,40]) wird ein Generator-Objekt erstellt.
4. Die for-Schleife iteriert über dieses Generator-Objekt und gibt jedes Quadrat aus.

### Was macht decorator_logging.py

1. Beim Aufruf von message("Max") wird der Dekorator aktiviert.
2. Der Dekorator führt die message-Funktion aus und erfasst das Ergebnis.
3. Der Funktionsaufruf wird mit Details in die Log-Datei geschrieben.
4. Das Ergebnis der Funktion wird zurückgegeben und ausgegeben.

### Was macht decorator_caching.py

1. Der memoize-Dekorator erstellt ein Cache-Dictionary für jede dekorierte Funktion.
2. Bei jedem Funktionsaufruf wird zuerst geprüft, ob das Ergebnis bereits im Cache ist.
3. Wenn ja, wird das gespeicherte Ergebnis zurückgegeben, ohne die Funktion erneut zu berechnen.
4. Wenn nicht, wird die Funktion ausgeführt, das Ergebnis im Cache gespeichert und zurückgegeben.
5. Die Fibonacci-Funktion nutzt diese Memoization, um wiederholte Berechnungen zu vermeiden.

### Was macht decorator_error_handling.py

1. Der Dekorator fängt alle Ausnahmen ab, die während der Ausführung der dekorierten Funktion auftreten könnten.
2. Bei jedem Aufruf von divide:
   - Wenn die Division erfolgreich ist, wird das Ergebnis zurückgegeben und ausgegeben.
   - Wenn eine Ausnahme auftritt (z.B. Division durch Null), wird die Fehlermeldung ausgegeben und 1 zurückgegeben.
