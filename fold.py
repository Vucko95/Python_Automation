from pathlib import Path

root_dir = Path('./Foldering')
file_paths = root_dir.iterdir()
# print(list(file_paths))


for path in file_paths:
    if path.is_file():
        new_file_name = (path.stem + 'TEST' + path.suffix)
        new_file_path = path.with_name(new_file_name)
        path.rename(new_file_path)
        print(new_file_path)


# print(list(file_paths))
