import os
import sys


def make_links_low_level(otkuda, kuda):
    try:
        os.mkdir(kuda)
    except FileExistsError:
        pass
    except:
        print(f"Ошибка создания {kuda}")
        return

    try:
        files = os.listdir(otkuda)
    except:
        print(f"Ошибка чтения {otkuda}")
        return

    for filename in files:
        source_path = os.path.join(otkuda, filename)
        target_path = os.path.join(kuda, filename)

        if os.path.isfile(source_path):
            try:

                os.link(source_path, target_path)
                print(f"Ссылка: {filename}")
            except OSError as e:
                print(f"Ошибка: {filename} - {e}")


make_links_low_level("./папка1", "./папка2")