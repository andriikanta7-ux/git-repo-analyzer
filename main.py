import os
import sys


def find_files(directory):
    """Збирає всі файли в каталозі та підкаталогах."""
    всі_файли = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            всі_файли.append(os.path.join(root, file))
    return всі_файли


def main():

    if len(sys.argv) == 1:
        repo_path = "."
        print("Шлях не вказано, візьму поточний каталог.")
    elif len(sys.argv) == 2:
        repo_path = sys.argv[1]
    else:
        print("Забагато аргументів! Треба тільки один шлях.")
        print("Usage: python main.py [repository_path]")
        sys.exit(1)


    if not os.path.exists(repo_path):
        print(f"Каталог '{repo_path}' не знайдено. Може, помилка в назві?")
        sys.exit(1)

    if os.path.isfile(repo_path):
        print("Це файл, а мені потрібен каталог. Не плутай мене!")
        sys.exit(1)

    print("Репозиторій: " + repo_path)
    print()

    файли = find_files(repo_path)

    if not файли:
        print("Тут порожньо, навіть файлика немає.")
    else:
        print("Знайдені файли:")
        for шлях in файли:
            print(шлях)
        print(f"\nРазом: {len(файли)} шт.")


if __name__ == "__main__":
    main()