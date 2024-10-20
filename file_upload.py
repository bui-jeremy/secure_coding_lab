import os

UPLOAD_DIRECTORY = "./uploads/"

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

# Insecure Code Example
# This code saves user-uploaded files directly without validating file types.
# Exploit the vulnerability by entering a filename like: ../../etc/passwd
filename = input("Enter the filename to upload (Try: ../../etc/passwd): ")
with open(os.path.join(UPLOAD_DIRECTORY, filename), 'w') as file:
    file.write("This is a test file.")
print(f"File saved to {os.path.join(UPLOAD_DIRECTORY, filename)}")

# Secure Code Example (commented out)
# Use filename sanitization to prevent directory traversal attacks.
'''
import os

UPLOAD_DIRECTORY = "./uploads/"
filename = input("Enter the filename to upload: ")
# Use basename to sanitize the filename and prevent directory traversal
safe_filename = os.path.basename(filename)
with open(os.path.join(UPLOAD_DIRECTORY, safe_filename), 'w') as file:
    file.write("This is a test file.")
print(f"File saved to {os.path.join(UPLOAD_DIRECTORY, safe_filename)}")
'''
