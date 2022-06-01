from pathlib import Path
from datetime import datetime

# root_dir = Path('./DateFileRenamer')
# path = Path('./DateFileRenamer/December/December-pmj.txt')
# file_paths = root_dir.glob("**/*")
# stats = path.stat()
# second_created = stats.st_ctime
# date_created = datetime.fromtimestamp(second_created)
# # date_created_str = str(date_created) # Easier way without format
# date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")

# print(date_created_str)

root_dir = Path('./DateFileRenamer/files')
file_paths = root_dir.glob("**/*")
for path in file_paths:
    if path.is_file():
        stats = path.stat()
        second_created = stats.st_ctime
        date_created = datetime.fromtimestamp(second_created)
        date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")
        new_file_name = date_created_str + '_' + path.name  # STRING OBJECT
        print(new_file_name)
        new_file_path = path.with_name(new_file_name)  # new PATH OBJECT
        print(new_file_path)
        # path.rename(new_file_path)
# Not working
