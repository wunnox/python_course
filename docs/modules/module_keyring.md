# Modul Keyring

Das Python-Modul `keyring` bietet eine einfache, einheitliche Schnittstelle, um Passwörter und andere Zugangsdaten sicher im jeweiligen System-Schlüsselbund zu speichern (z.B. Windows Credential Manager, macOS Keychain oder Secret Service unter Linux). Statt Passwörter im Klartext in Skripten oder Konfigurationsdateien abzulegen, greift der Python-Code über keyring auf die vom Betriebssystem bereitgestellten, geschützten Speichermechanismen zu.

## Beispiel:

```python
import keyring

service = "my-demo-service"
username = "alice"

# Save your password securely in the system keychain
keyring.set_password(service, username, "TopSecret123!")

# Read the password from the keyring later
pwd = keyring.get_password(service, username)

print(f"User: {username}")
print(f"Password from Keyring: {pwd}")
```

Download: [module_keyring.py](../examples/modules/module_keyring.py)

> Hinweis:
> Das Erfassen von Passwörtern sollte in gesonderten Skripts erfolgen, welche an einem sicheren Ort aufbewahrt werden müssen.

