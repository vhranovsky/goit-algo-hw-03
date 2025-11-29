import sys
import shutil
from pathlib import Path


def copy_file(file_path: Path, output_folder: Path):
    try:

        extension = file_path.suffix[1:] if file_path.suffix else "no_ext"

        target_folder = output_folder / extension
        target_folder.mkdir(parents=True, exist_ok=True)
        target_path = target_folder / file_path.name

        shutil.copy2(file_path, target_path)
        print(f"[OK] Копіюю: {file_path} -> {target_path}")

    except PermissionError:
        print(f"[ERROR] Немає прав доступу до файлу: {file_path}")
    except OSError as e:
        print(f"[ERROR] Помилка ОС при копіюванні {file_path}: {e}")
    except Exception as e:
        print(f"[ERROR] Невідома помилка з файлом {file_path}: {e}")


def read_folder(path: Path, output_folder: Path):
    try:
        if not path.exists():
            print(f"[ERROR] Директорія {path} не існує.")
            return

        for item in path.iterdir():
            if item.is_dir():
                read_folder(item, output_folder)
            elif item.is_file():
                copy_file(item, output_folder)

    except PermissionError:
        print(f"[ERROR] Немає прав доступу до директорії: {path}")
    except OSError as e:
        print(f"[ERROR] Помилка доступу до {path}: {e}")


def main():
    if len(sys.argv) < 2:
        print("Помилка: Відсутній обовязковий параметр <шлях до вихідної директорії>.")
        print("Використання: python honme_task1.py <source_folder> [output_folder]")
        sys.exit(1)

    # Перший аргумент - вихідна папка
    source_path = Path(sys.argv[1])

    # Другий аргумент - папка призначення (необов'язковий)
    # Якщо аргументу немає, використовуємо 'dist'
    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2])
    else:
        output_path = Path("dist")

    read_folder(source_path, output_path)


if __name__ == "__main__":
    main()
