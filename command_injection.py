import os

# Insecure Code Example
# This code is vulnerable to command injection because it directly includes user input in the system command.
# To exploit the vulnerability:
# Enter the following input when prompted: ; ls
command = input("Enter a file name to check existence (Try entering: ; ls): ")
os.system(f"echo Checking file: {command}")

# Secure Code Example (commented out)
# To prevent command injection, use a more secure method like subprocess with a list of arguments.
'''
import subprocess

command = input("Enter a file name to check existence: ")
subprocess.run(["echo", "Checking file:", command])
'''
