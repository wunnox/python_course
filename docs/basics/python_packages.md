# Python Pakete

Um in Python ein Paket zu erstellen, braucht es folgende Schritten:

## Verzeichnisstruktur erstellen

Erstellen Sie eine Verzeichnisstruktur für Ihr Paket. Ein einfaches Beispiel könnte so aussehen:

```text
my_package/
    ├── my_package/
    │   ├── __init__.py
    │   ├── module1.py
    │   └── module2.py
    ├── tests/
    ├── README.md
    ├── LICENSE
    └── pyproject.toml
```

## init.py Datei erstellen

Die `__init__.py` Datei im Hauptverzeichnis Ihres Pakets ist entscheidend. Sie kann leer sein oder Code enthalten, der beim Importieren des Pakets ausgeführt wird.

## Module erstellen

Erstellen Sie Python-Dateien (.py) als die verschiedenen Module Ihres Pakets.

## pyproject.toml Datei erstellen

Die `pyproject.toml` Datei ist wichtig für die Konfiguration des Build-Systems und die Metadaten des Pakets. Hier ein Beispiel:

```text
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mein_paket"
version = "0.0.1"
authors = [
  { name="Ihr Name", email="ihre.email@example.com" },
]
description = "Eine kurze Beschreibung Ihres Pakets"
readme = "README.md"
requires-python = ">=3.10"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/yourusername/mein_paket"
"Bug Tracker" = "https://github.com/yourusername/mein_paket/issues"
```

Download: [pyproject.toml](../examples/basics/pyproject.toml)

## README.md und LICENSE Dateien erstellen

Erstellen Sie eine `README.md` Datei mit einer Beschreibung Ihres Pakets und Nutzungsanweisungen. Fügen Sie auch eine `LICENSE` Datei hinzu, die die Nutzungsbedingungen Ihres Pakets festlegt.

## Paket bauen

Verwenden Sie das build Modul, um Distributionsdateien zu erstellen:

```bash
python -m pip install --upgrade build
python -m build
```

Dies erstellt eine .whl Datei (Wheel) und eine .tar.gz Datei im dist/ Verzeichnis.

## Paket testen

Testen Sie Ihr Paket lokal, indem Sie es in einer virtuellen Umgebung installieren:

```bash
python -m venv test_env
source test_env/bin/activate  # Auf Windows: test_env\Scripts\activate
pip install dist/mein_paket-0.0.1-py3-none-any.whl
```

## Paket veröffentlichen (optional)

Wenn Sie Ihr Paket auf PyPI veröffentlichen möchten, können Sie das `twine` Tool verwenden:

```bash
python -m pip install --upgrade twine
python -m twine upload dist/*
```

> Hinweis: 
> Beachten Sie, dass Sie für diesen Schritt ein Konto auf PyPI benötigen.
