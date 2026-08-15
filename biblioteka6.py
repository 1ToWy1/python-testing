def book_list_view(lib):
    if not lib:
        print("Библиотека пуста")
        return

    for book in lib:
        print(book)


def add_book(lib, title, author, year):
    if not title.strip():
        print("Ошибка: Название книги не может быть пустым")
        return

    if not author.strip():
        print("Ошибка: Имя автора не может быть пустым")
        return

    try:
        year = int(year)
        if not (0 <= year <= 2026):
            print("Ошибка: Некорректный год издания")
            return
    except ValueError:
        print("Ошибка: Год издания должен быть числом")
        return

    title = title.strip()
    status = None
    action_text = "успешно добавлена"

    if title in lib:
        print(f"Книга '{title}' уже существует в библиотеке.")
        choice = input("Хотите обновить информацию? (да/нет): ").strip().lower()
        if choice != "да":
            print("Операция отменена")
            return

        status = lib[title]["наличие"]
        action_text = "обновлена"

    lib[title] = {
        "автор": author.strip(),
        "год издания": year,
        "наличие": status
    }
    print(f"Информация о книге '{title}' {action_text}")


def remove_book(lib, title):
    if not title.strip():
        print("Ошибка: Название книги не может быть пустым")
        return

    title = title.strip()

    if title not in lib:
        print(f"Ошибка: Книга '{title}' не найдена в библиотеке")
        return

    del lib[title]
    print(f"Книга '{title}' успешно удалена")


def issue_book(lib, title):
    if not title.strip():
        print("Ошибка: Название книги не может быть пустым")
        return

    title = title.strip()

    if title not in lib:
        print(f"Ошибка: Книга '{title}' не найдена в библиотеке")
        return

    if lib[title]["наличие"] is False:
        print(f"Ошибка: Книга '{title}' уже выдана!")
        return

    lib[title]["наличие"] = False
    print(f"Книга '{title}' выдана")


def return_book(lib, title):
    if not title.strip():
        print("Ошибка: Название книги не может быть пустым")
        return

    title = title.strip()

    if title not in lib:
        print(f"Ошибка: Книга '{title}' не найдена в библиотеке")
        return

    if lib[title]["наличие"] is True or lib[title]["наличие"] == "в наличии":
        print(f"Ошибка: Книга '{title}' уже находится в библиотеке!")
        return

    lib[title]["наличие"] = True
    print(f"Книга '{title}' возвращена в библиотеку")


def find_book(lib, title):
    if not title.strip():
        print("Ошибка: Название книги не может быть пустым")
        return

    title = title.strip()

    if title not in lib:
        print(f"Ошибка: Книга '{title}' не найдена в библиотеке")
        return

    book_info = lib[title]
    status = book_info["наличие"]

    statuses = {
        None: "Книга в библиотеке, но ее статус не определен",
        False: "Книга выдана",
        True: "Книга доступна"
    }

    status_text = statuses.get(status, str(status))

    print(f"Информация о книге '{title}':")
    print(f"  Автор: {book_info['автор']}")
    print(f"  Год издания: {book_info['год издания']}")
    print(f"  Статус: {status_text}")


def handle_add_book(lib):
    t = input("Введите название книги: ")
    a = input("Введите автора: ")
    y = input("Введите год издания: ")
    add_book(lib, t, a, y)


def handle_remove_book(lib):
    t = input("Введите название книги для удаления: ")
    remove_book(lib, t)


def handle_issue_book(lib):
    t = input("Введите название книги для выдачи: ")
    issue_book(lib, t)


def handle_return_book(lib):
    t = input("Введите название книги для возврата: ")
    return_book(lib, t)


def handle_find_book(lib):
    t = input("Введите название книги для поиска: ")
    find_book(lib, t)


def main_menu():
    menu = {
        "1": ("Просмотреть список книг", book_list_view),
        "2": ("Добавить книгу", handle_add_book),
        "3": ("Удалить книгу", handle_remove_book),
        "4": ("Выдать книгу", handle_issue_book),
        "5": ("Вернуть книгу", handle_return_book),
        "6": ("Найти книгу", handle_find_book),
        "0": ("Выход", None)
    }

    while True:
        print("\n--- Главное меню ---")
        for key, (title, _) in menu.items():
            print(f"{key}. {title}")

        choice = input("Выберите действие: ").strip()

        if choice not in menu:
            print("Некорректный ввод, попробуйте снова.")
            continue

        if choice == "0":
            print("До свидания!")
            break

        _, action = menu[choice]
        action(library)


library = {
    "Мастер и Маргарита": {
        "автор": "Михаил Булгаков",
        "год издания": 1967,
        "наличие": "в наличии"
    },
    "Преступление и наказание": {
        "автор": "Федор Достоевский",
        "год издания": 1866,
        "наличие": None
    }
}


if __name__ == "__main__":
    main_menu()
