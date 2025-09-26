import os
from pathlib import Path

def change_extensions(papka, staroe, novoe):
    for file in Path(papka).iterdir():
        if file.is_file() and file.suffix == staroe:
            novoe_imya = file.with_suffix(novoe)
            file.rename(novoe_imya)
            print(f"Переименовал: {file.name} -> {novoe_imya.name}")

change_extensions("../папка", ".txt", ".doc")