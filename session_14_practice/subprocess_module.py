import subprocess

result = subprocess.run(["echo", "Hello"], capture_output=True, text=True)
print(result)