import sys
import socket

if len(sys.argv) != 2:
  print("Please enter a file to redirect hostname.")
else:
  hostname = socket.gethostname()
  filename = sys.argv[1]
  
  with open(filename, "w") as f:
      f.write(hostname)

  print("Hostname is written successfully.")
