import os
import shutil
from datetime import datetime

source_dir = "sample_dir"

backup_dir = "backup_dir"

timestamp = datetime.now().strftime("%Y%m%d_%H%M")

backup_archive_name = os.path.join(backup_dir, f"backup_{timestamp}")

shutil.make_archive(backup_archive_name, "zip", source_dir)

archive_exist = os.path.exists(f"{backup_archive_name}.zip")

print(archive_exist)