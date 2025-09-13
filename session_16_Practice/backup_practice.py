import os
import shutil
from datetime import datetime

# method 1
# source_dir = f"session_15_Practice"
# destination_dir = f"backup"

# method 2
base_dir = "/home/wasim/python_dir"
source_dir = f"{base_dir}/session_15_Practice"
destination_dir = f"{base_dir}/backup"
os.makedirs(destination_dir, exist_ok=True)
timestamp = datetime.now().strftime("%d-%m-Y_%H-%M-%S")

backup_file_name = os.path.join(destination_dir, f"session_15_practice_backup-{timestamp}")

shutil.make_archive(backup_file_name, 'zip', source_dir)

print(f"Backup created: {backup_file_name}.zip")
