import os, subprocess

output = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(output.stdout)
print(os.listdir())

temp_dir = "temp_dir"

if not os.path.exists(temp_dir):
  os.mkdir(temp_dir)
  print("Directory created")

# os.rename(temp_dir, "temp2_dir")
with open("text_file2.txt", "w") as f:
  f.write("Hii wasim")


os.rmdir(temp_dir)