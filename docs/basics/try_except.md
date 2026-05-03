# try - except

`try/except` wird in Python zur Fehlerbehandlung benutzt.
 - Im `try`‑Block steht Code, der eine Ausnahme (Exception) auslösen könnte.
 - Tritt ein Fehler auf, wird der `try`‑Block abgebrochen und der passende `except`‑Block ausgeführt, statt dass das Programm abstürzt.
 - Ohne Fehler wird der `except`‑Block übersprungen und das Programm normal fortgesetzt.

## Beispielscript

```python
def read_a_number_from_file(path):
    try:
        f = open(path, "r")
        contents = f.read()
        number = int(contents)              # may raise a ValueError
    except FileNotFoundError:
        print("File not found")
        return None
    except ValueError:
        print("The value is not a whole number")
        return None
    except Exception as e:
        print("The following error has occurred:",e)
    else:
        print("Number read successfully:", number)
        return number
    finally:
        # Always executed – regardless of whether there is an error or not
        try:
            f.close()
            print("Close file")
        except UnboundLocalError:
            # f was never created (e.g. in the case of a FileNotFoundError before the open operation)
            pass

read_a_number_from_file("number.txt")
```

Download: [try_except.py](../examples/basics/try_except.py)

### Erklärung

- Im `try`‑Block wird die Datei geöffnet, ihr Inhalt gelesen und mit `int(...)` in eine ganze Zahl umgewandelt. Hier können sowohl Datei‑ als auch Konvertierungsfehler auftreten.
- Der erste `except FileNotFoundError` fängt den Fall ab, dass die Datei nicht existiert, meldet das und gibt None zurück. (Optional)
- Der zweite `except ValueError` behandelt den Fall, dass der gelesene Inhalt keine gültige ganze Zahl ist, meldet dies ebenfalls und gibt None zurück. (Optional)
- Der `else`‑Block wird nur ausgeführt, wenn im `try` kein Fehler auftritt: Die Zahl wurde erfolgreich gelesen und wird ausgegeben und zurückgegeben. (Optional)
- Der `finally`‑Block läuft immer, egal ob ein Fehler aufgetreten ist oder nicht, und versucht die Datei wieder zu schließen; falls f wegen eines frühen Fehlers gar nicht existiert, wird der `UnboundLocalError` still ignoriert. So wird sichergestellt, dass Ressourcen (hier die Datei) zuverlässig aufgeräumt werden. (Optional)
- Der Block `except Exception as e` braucht es mindestens, wenn sonst kein `except`-Block existiert. Ist auch nur als `except` möglich. Die anderen Blöcke sind optional und können bei Bedarf auch weggelassen werden. 
