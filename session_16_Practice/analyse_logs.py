import re

with open('app.log', 'r') as f:
  for line in f:
    if "ERROR" in line or "CRITICAL" in line:
      print(f"{line.strip()}")

pattern = re.compile(r'.* - (ERROR|CRITICAL) - *')
print("Pattern: ", pattern)
with open('app.log', 'r') as f:
  for line in f:
    if pattern.match(line):
      print(line.strip())