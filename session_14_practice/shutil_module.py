import shutil

def check_disk(disk):
  return shutil.disk_usage(disk)


print(check_disk('/'))