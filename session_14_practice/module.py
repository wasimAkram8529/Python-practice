import os, subprocess

output = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(output.stdout)
print(os.listdir())