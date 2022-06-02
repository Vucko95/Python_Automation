from pathlib import Path
import zipfile
root_dir = Path('./FileZiper/')
destination_path = Path('.')
archive_path = root_dir.glob("*.zip")
for path in archive_path:
    with zipfile.ZipFile(path, 'r') as zf:
        zf.extractall(destination_path)
