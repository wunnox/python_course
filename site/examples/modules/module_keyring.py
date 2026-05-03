import keyring

service = "my-demo-service"
username = "alice"

# Save your password securely in the system keychain
keyring.set_password(service, username, "TopSecret123!")

# Read the password from the keyring later
pwd = keyring.get_password(service, username)

print(f"User: {username}")
print(f"Password from Keyring: {pwd}")
