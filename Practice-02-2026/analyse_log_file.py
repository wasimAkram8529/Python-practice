import re

# with open("example.log", "r") as file:
#   for line in file:
#     print(line.strip())

base_dir = "log-files"
with open(f"{base_dir}/example.log", "r") as file:
  for line in file:
    if re.search(r"ERROR", line):
      print(line.strip())

