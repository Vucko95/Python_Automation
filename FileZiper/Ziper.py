from pathlib import Path
import zipfile
root_dir = Path('./FileZiper/')
archive_path = root_dir / Path('archive.zip')
files = root_dir.rglob("*.txt")
with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in files:
        zf.write(path)
        # path.unlink()  # This can be used to delete fiels that are archived
