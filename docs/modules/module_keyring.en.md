# Module Keyring

The Python keyring module provides a simple, unified interface for securely storing passwords and other credentials in the relevant system keychain (e.g. Windows Credential Manager, macOS Keychain or Secret Service on Linux). Instead of storing passwords in plain text in scripts or configuration files, the Python code uses keyring to access the secure storage mechanisms provided by the operating system.

## Example script

- [module_keyring.py](../examples/modules/module_keyring.py) 
