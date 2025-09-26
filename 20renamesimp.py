import os

def change_extensions_very_low(papka, staroe, novoe):
    try:
        all_items = os.listdir(papka)
    except OSError as e:
        print(f"Ошибка доступа к {papka}: {e}")
        return

    for item in all_items:
        full_path = os.path.join(papka, item)

        if os.path.isfile(full_path) and item.endswith(staroe):
            if '.' in item:
                base_name = item.rsplit('.', 1)[0]
            else:
                base_name = item

            new_name = base_name + novoe
            new_path = os.path.join(papka, new_name)

            try:
                os.rename(full_path, new_path)
                print(f"{item} -> {new_name}")
            except OSError as e:
                print(f"Ошибка: {item} - {e}")

change_extensions_very_low("../папка", ".txt", ".doc")