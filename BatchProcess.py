# This is a fire and forget batch processor that will run multiple python scripts listed in the commands table with the arguments following commands

import subprocess

# Define a list of commands to execute
commands = [
    ["python", "easyOCRtest.py", "1809", "1811"],
    ["python", "easyOCRtest.py", "1908", "1917"],
    ["python", "easyOCRtest.py", "1960", "1972"],
    ["python", "easyOCRparsing.py", "1809out"],
    ["python", "easyOCRparsing.py", "1908out"],
    ["python", "easyOCRparsing.py", "1960out"],
]

# Run each command in the list
for cmd in commands:
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}\n{e}")



