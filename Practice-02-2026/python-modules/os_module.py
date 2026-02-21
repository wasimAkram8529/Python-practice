import os


# create a file
with open("example.txt", "w") as f:
  f.write("Hello from example text file")

# modify a file
with open("example.txt", "w") as f:
  f.write("Modified file")

# rename file
os.rename("example.txt", "example_2.txt")

# os.remove("example_2.txt")
# print(os.getcwd())
# print(os.listdir())