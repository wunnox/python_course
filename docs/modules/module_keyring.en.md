# Module Keyring

The Python `keyring` module provides a simple, unified interface for securely storing passwords and other credentials in the relevant system keychain (e.g. Windows Credential Manager, macOS Keychain or Secret Service on Linux). Instead of storing passwords in plain text in scripts or configuration files, the Python code uses keyring to access the secure storage mechanisms provided by the operating system.

## Example:

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

> Note:
> Passwords should be recorded in separate scripts, which must be kept in a secure location.
