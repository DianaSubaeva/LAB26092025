from pathlib import Path
import os

def make_links(from_dir, to_dir):
    Path(to_dir).mkdir(exist_ok=True)

    for file in Path(from_dir).iterdir():
        if file.is_file():
            try:
                os.link(file, Path(to_dir) / file.name)
                print(f"Создал: {file.name}")
            except:
                print(f"Ошибка: {file.name}")


make_links("./папка1", "./папка2")