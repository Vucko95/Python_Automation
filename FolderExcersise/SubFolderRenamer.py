from pathlib import Path

root_dir = Path('./FolderExcersise/files')
file_paths = root_dir.glob("**/*")
for path in file_paths:
    if path.is_file():
        path_parts = path.parts
        # print(path_parts)
        # print("---")
        subfolders = path.parts[2:-1]
        print(subfolders)

        new_file_name = "-".join(subfolders) + '-' + path.name  # STRING OBJECT
        print(new_file_name)

        new_file_path = path.with_name(new_file_name)  # new PATH OBJECT
        path.rename(new_file_path)
