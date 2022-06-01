from pathlib import Path

root_dir = Path('./DateFileRenamer/files/December')
file_paths = root_dir.rglob("*.csv")
for path in file_paths:
    if path.is_file():
        # print(path)
        path_name_suffix = path.with_suffix('.txt')
        path.rename(path_name_suffix)
