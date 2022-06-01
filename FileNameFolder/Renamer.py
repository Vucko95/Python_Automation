from pathlib import Path

root_dir = Path('./FileNameFolder')
file_paths = root_dir.glob("**/*")
for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2]
        # print(parent_folder)
        new_file_name = parent_folder + '-' + path.name
        # print(new_file_name)
        new_file_path = path.with_name(new_file_name)
        path.rename(new_file_path)
