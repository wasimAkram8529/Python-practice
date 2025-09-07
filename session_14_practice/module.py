import os, subprocess

output = subprocess.run(["ls", "-l"])
print(output.stdout)
print(os.listdir())