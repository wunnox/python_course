# Dekoratoren

Dekoratoren sind eine elegante Möglichkeit, Funktionen oder Klassen um zusätzliche Funktionalität zu erweitern, ohne den Originalcode anzupassen.

Die wichtigsten Punkte sind:

 - Erweiterung von Funktionen ohne Codeänderung.
 - Wiederverwendbarer Code für Logging, Caching, Validierung oder Timing.
 - Bessere Struktur und weniger Code-Duplikation.

## Funktionsweise von Dekoratoren

Dekoratoren sind im Grunde nur verschachtelte Funktionen.

```python
def inner_function():
    print("I am the inner_function")

def outer_function():
    print(f"I am the outer_function and run {inner_function}")
    return inner_function

func = outer_function()

func()
```

Es wird eine Funktion aufgerufen (`outer_function`), welche wiederum eine Funktion aufruft (`inner_function`).

Die `outer_function` wird in der Regel `wrapper` genannt. Dem `wrapper` wird als Argument der Name der `inner_function` übergeben.

```python
def func1():
    print("I am function func1")

def add_wrapper(fn):
    def wrapper(*args, **kwargs):
        print(f"I am the wrapper and run {fn}")
        return(fn(*args, **kwargs))
    return wrapper

func1 = add_wrapper(func1)

func1() 
```

## Beispielscripts

### Zeitmessung

Performancemessung einer Funktion

1. Der timer_decorator misst die Zeit, die für die Ausführung der dekorierten Funktion benötigt wird.
2. Die `square-Funktion` ist ein Generator, der Quadrate der Eingabezahlen erzeugt.
3. Beim Aufruf von `square([10,20,30,40])` wird ein Generator-Objekt erstellt.
4. Die `for`-Schleife iteriert über dieses Generator-Objekt und gibt jedes Quadrat aus.

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Runtime of {func.__name__}: {round(end_time - start_time,6)} Seconds")
        return result
    return wrapper

@timer_decorator
def square(n):
   for i in n:
      yield (i*i)

res=square([10,20,30,40])
for number in res:
   print(number)
```
Download: [decorator_time.py](../examples/basics/decorator_time.py)

### Logging

Ausgabe einer Funktion loggen

- Beim Aufruf von `message("Max")` wird der Dekorator aktiviert.
- Der Dekorator führt die `message`-Funktion aus und erfasst das Ergebnis.
- Der Funktionsaufruf wird mit Details in die Log-Datei geschrieben.
- Das Ergebnis der Funktion wird zurückgegeben und ausgegeben.

```python
import logging   
  
logging.basicConfig(  
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S',  
    filename='decorator_test.log'  
    )  
logger = logging.getLogger('test_logger')  
  
def log_function_call(func):  
    def wrapper(*args, **kwargs):  
        result = func(*args, **kwargs)  
        log_message=f"Function {func.__name__} called Argument {args}. Result: {result}"  
        logger.info(log_message)  
        return result  
    return wrapper  
  
@log_function_call  
def message(name):  
    return f"Hello, {name}!"  
  
print(message("Max"))       
```

Download: [decorator_logging.py](../examples/basics/decorator_logging.py)

### Caching

Berechnung per Caching beschleunigen

 - Der `memoize`-Dekorator erstellt ein Cache-Dictionary für jede dekorierte Funktion.
 - Bei jedem Funktionsaufruf wird zuerst geprüft, ob das Ergebnis bereits im Cache ist.
 - Wenn ja, wird das gespeicherte Ergebnis zurückgegeben, ohne die Funktion erneut zu berechnen.
 - Wenn nicht, wird die Funktion ausgeführt, das Ergebnis im Cache gespeichert und zurückgegeben.
 - Die Fibonacci-Funktion nutzt diese Memoization, um wiederholte Berechnungen zu vermeiden.

```python
from time import perf_counter

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# Deactivate the next line to see the difference
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start = perf_counter()
for i in range(40):
    print(fibonacci(i))
end = perf_counter()

print("Runtime:", round(end - start,6), "Sec")
```

### Fehler Handling

Abfangen von Fehler in einer Funktion

- Der Dekorator fängt alle Ausnahmen ab, die während der Ausführung der dekorierten Funktion auftreten könnten.
- Bei jedem Aufruf von divide:
    - Wenn die Division erfolgreich ist, wird das Ergebnis zurückgegeben und ausgegeben.
    - Wenn eine Ausnahme auftritt (z.B. Division durch Null), wird die Fehlermeldung ausgegeben und 1 zurückgegeben.

```python
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in Function {func.__name__}: {str(e)}, return 1")
            return 1
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

for i in (3,0,7):
    print(divide(10, i))
```

Download: [decorator_error_handling.py](../examples/basics/decorator_error_handling.py)

