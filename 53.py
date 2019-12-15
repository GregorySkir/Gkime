from pathlib import Path
def count_files(folder=Path.home()):
    if Path.is_dir(folder) == False:
        return (0,0)
    count_file = 0
    count_dir = 0
    f = Path(folder)
    if f.exists():
        for item in f.iterdir():
            if item.is_file():
               count_file += 1
            else:
               count_dir += 1
    return (count_dir, count_file)
print(count_files())