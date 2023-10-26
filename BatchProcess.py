# This is a fire and forget batch processor that will run multiple python scripts listed in the commands table with the arguments following commands

import subprocess

# Define a list of commands to execute
commands = [
    ["python", "easyOCRtest.py", "1992", "1999"],
    ["python", "easyOCRparsing.py", "1992out"]
]

# Run each command in the list
for cmd in commands:
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}\n{e}")
