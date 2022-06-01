from pathlib import Path

root_dir = Path('./DateFileRenamer/files')
for i in range(1, 5):
    filename = str(i) + '.txt'
    filepath = root_dir / Path(filename)
    filepath.touch()
