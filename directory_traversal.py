import os

# Insecure Code Example
# This code is vulnerable to directory traversal attacks because it allows unfiltered file path input.
# To exploit the vulnerability:
# Enter the following input when prompted: ../../etc/passwd
file_path = input("Enter the file name to read (Try ../../etc/passwd): ")
with open(file_path, 'r') as file:
    print(file.read())

# Secure Code Example (commented out)
# Prevent directory traversal by restricting the file path to a safe directory.
'''
import os

base_directory = '/safe_directory/'
file_path = input("Enter the file name to read: ")
safe_path = os.path.join(base_directory, os.path.basename(file_path))
with open(safe_path, 'r') as file:
    print(file.read())
'''
