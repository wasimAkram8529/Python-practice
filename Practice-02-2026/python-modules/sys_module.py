import sys

print(sys.platform)
print("All argument: ", sys.argv)

if len(sys.argv) > 1:
  print("First argument: ", sys.argv[1] + " " + sys.argv[2])
else:
  print("No argument provided")
