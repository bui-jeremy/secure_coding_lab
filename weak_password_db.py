import hashlib

# Insecure Code Example
# This code stores passwords in plaintext, making them vulnerable if the database is compromised.
password = input("Enter your password to store: ")
print(f"Storing password: {password}")  # This is insecure

# Secure Code Example (commented out)
# Use a secure hashing function with a salt to store passwords securely.
'''
salt = "random_salt_value"
hashed_password = hashlib.sha256((salt + password).encode()).hexdigest()
print(f"Storing secure password hash: {hashed_password}")
'''
