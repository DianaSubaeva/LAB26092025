from pathlib import Path
import time

def monitor(folder='.'):
    files = {f.name: f.stat().st_mtime for f in Path(folder).iterdir() if f.is_file()}
    print("Мониторинг запущен...")

    try:
        while True:
            current = {f.name: f.stat().st_mtime for f in Path(folder).iterdir() if f.is_file()}

            current_keys = set(current.keys())
            files_keys = set(files.keys())

            for name in current_keys - files_keys:
                print(f"Создан: {name}")

            for name in files_keys - current_keys:
                print(f"Удален: {name}")

            for name in current_keys & files_keys:
                if current[name] != files[name]:
                    print(f"Изменен: {name}")

            files = current
            time.sleep(1)
    except KeyboardInterrupt:
        print("Остановлено")

monitor()

