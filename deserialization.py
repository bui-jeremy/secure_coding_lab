import pickle

# Insecure Code Example
# This code is vulnerable to insecure deserialization, which can execute arbitrary code.
# To exploit the vulnerability, a malicious user could craft a pickle payload.
data = input("Enter some data to serialize (Be cautious!): ")
serialized_data = pickle.dumps(data)
print("Serialized data:", serialized_data)

# Secure Code Example (commented out)
# Avoid using pickle for untrusted input. Use a safer serialization format like JSON.
'''
import json

data = input("Enter some data to serialize: ")
serialized_data = json.dumps(data)
print("Serialized data:", serialized_data)
'''
