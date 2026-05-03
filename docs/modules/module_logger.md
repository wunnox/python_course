# Modul Logger

Mit diesem Module können Logmeldungen erzeugt werden

```python
import logging

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='Example.log'
    )
logger = logging.getLogger('my_logger')

name='Max'
print(f"Hello {name}")
logger.info(f'Hello {name}')
```

Download: [logger.py](../examples/modules/module_logger.py)

## Erklärung:

Dies Zeilen in der Funktion konfigurieren das grundlegende Logging-System:

 - level=logging.INFO: Setzt das Logging-Level auf INFO. Dies bedeutet, dass Nachrichten mit den Levels INFO, WARNING, ERROR und CRITICAL protokolliert werden.
 - format=...: Definiert das Format der Log-Einträge. Hier werden Zeitstempel, Logger-Name, Log-Level und die eigentliche Nachricht einbezogen.
 - datefmt='%Y-%m-%d %H:%M:%S': Legt das Format für den Zeitstempel fest.
 - filename='apply.log': Gibt an, dass die Log-Einträge in eine Datei namens 'apply.log' geschrieben werden sollen.

Anschliessend wird eine Loggmeldung erstellt:

 - name='Peter': Weist der Variable name den Wert 'Peter' zu.
 - print(f"Hello {name}"): Gibt "Hello Peter" auf der Konsole aus.
 - logger.info(f'Hello {name}'): Schreibt einen Log-Eintrag mit dem Level INFO und dem Text "Hello Peter" in die Log-Datei.

```text
2024-11-01 12:34:56 - my_logger - INFO - Hello Peter
```

## Verfügbare Logglevels

Das Python-Logging-Modul bietet fünf Hauptlogging-Levels, die in aufsteigender Reihenfolge der Schwere angeordnet sind. Diese Levels sind:

1. DEBUG (10)
2. INFO (20)
3. WARNING (30)
4. ERROR (40)
5. CRITICAL (50)

Hier sind die Details zu jedem Level:

DEBUG (10)
Dies ist das niedrigste Logging-Level. Es wird verwendet, um detaillierte Informationen für die Diagnose von Problemen bereitzustellen. Typischerweise wird es während der Entwicklung und beim Debugging eingesetzt.

INFO (20)
Dieses Level wird für allgemeine Informationen verwendet, die bestätigen, dass das Programm wie erwartet funktioniert.

WARNING (30)
WARNING ist das Standardlogging-Level. Es wird verwendet, um anzuzeigen, dass etwas Unerwartetes aufgetreten ist oder in naher Zukunft ein Problem auftreten könnte (z.B. "Disk space low").

ERROR (40)
Dieses Level wird verwendet, wenn ein ernsthaftes Problem aufgetreten ist, das die Ausführung einer bestimmten Funktion verhindert hat.

CRITICAL (50)
Dies ist das höchste Logging-Level. Es wird verwendet, um sehr schwerwiegende Fehler zu protokollieren, die möglicherweise dazu führen, dass das Programm nicht mehr ausgeführt werden kann

Es ist wichtig zu beachten, dass jedes Level numerische Werte hat (in Klammern angegeben), die seine Schwere repräsentieren. Ein Logger oder Handler mit einem bestimmten Level wird alle Nachrichten dieses Levels und höher protokollieren. Zusätzlich gibt es noch ein spezielles Level:

NOTSET (0)
Dieses Level wird verwendet, wenn kein spezifisches Level für einen Logger gesetzt wurde. In diesem Fall verwendet der Logger das Level seines Eltern-Loggers

Bei der Konfiguration des Loggings können Sie das gewünschte Level festlegen, um zu kontrollieren, welche Arten von Nachrichten protokolliert werden sollen. Zum Beispiel, wenn Sie das Level auf WARNING setzen, werden nur Nachrichten der Level WARNING, ERROR und CRITICAL protokolliert, während DEBUG und INFO ignoriert werden.
