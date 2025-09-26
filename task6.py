import os
import time
def advanced_monitor(path="."):
    file_states = {}

    # Начальное состояние
    for file in os.listdir(path):
        if os.path.isfile(file):
            full_path = os.path.join(path, file)
            file_states[file] = os.path.getmtime(full_path)

    print("Мониторинг запущен...")

    try:
        while True:
            current_files = set(os.listdir(path))

            # Проверка новых файлов
            for file in current_files - set(file_states.keys()):
                if os.path.isfile(os.path.join(path, file)):
                    print(f"Создан: {file}")
                    file_states[file] = os.path.getmtime(os.path.join(path, file))

            # Проверка удаленных файлов
            for file in set(file_states.keys()) - current_files:
                print(f"Удален: {file}")
                del file_states[file]

            # Проверка изменений файлов
            for file in file_states:
                if file in current_files and os.path.isfile(os.path.join(path, file)):
                    current_time = os.path.getmtime(os.path.join(path, file))
                    if current_time != file_states[file]:
                        print(f"Изменен: {file}")
                        file_states[file] = current_time

            time.sleep(1)

    except KeyboardInterrupt:
        print("Остановлено")


# Запуск
advanced_monitor()