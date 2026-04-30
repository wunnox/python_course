# Modul Keyring

Das Python-Modul keyring bietet eine einfache, einheitliche Schnittstelle, um Passwörter und andere Zugangsdaten sicher im jeweiligen System-Schlüsselbund zu speichern (z.B. Windows Credential Manager, macOS Keychain oder Secret Service unter Linux). Statt Passwörter im Klartext in Skripten oder Konfigurationsdateien abzulegen, greift der Python-Code über keyring auf die vom Betriebssystem bereitgestellten, geschützten Speichermechanismen zu.

## Beispielscript

- [module_keyring.py](../examples/modules/module_keyring.py)

