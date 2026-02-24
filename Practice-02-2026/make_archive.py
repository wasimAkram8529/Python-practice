import os
import shutil

os.makedirs('sample_dir', exist_ok=True)
with open("sample_dir/file1.txt", "w") as f:
  f.write("This is a sample file 1")

with open("sample_dir/file2.txt", "w") as f:
  f.write("This is a sample file 2")

shutil.make_archive("sample_archive", "zip", "sample_dir")

archive_exist = os.path.exists("sample_archive.zip")

print(archive_exist)