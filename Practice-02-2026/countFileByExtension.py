import os
import sys

def count_file_extension():
  if len(sys.argv) != 3:
    print("Please enter dirname and extension to count file by extension")
    return 0
  
  directoryName = sys.argv[1]
  extension = sys.argv[2]

  file_count = 0

  for dirpath, dirname, filename in os.walk(directoryName):
    print(dirpath)
    print(dirname)
    print(filename)
    for file in filename:
      if file.endswith(extension):
         file_count += 1

  return file_count

file_count = count_file_extension()
print(file_count)