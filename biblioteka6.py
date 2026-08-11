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

    if status is None:
        status_text = "Книга в библиотеке, но ее статус не определен"
    elif status is False:
        status_text = "Книга выдана"
    elif status is True:
        status_text = "Книга доступна"
    else:
        status_text = str(status)

    print(f"Информация о книге '{title}':")
    print(f"  Автор: {book_info['автор']}")
    print(f"  Год издания: {book_info['год издания']}")
    print(f"  Статус: {status_text}")


# Вспомогательные функции для обработки пользовательского ввода в меню
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
    menu_titles = {
        "1": "Просмотреть список книг",
        "2": "Добавить книгу",
        "3": "Удалить книгу",
        "4": "Выдать книгу",
        "5": "Вернуть книгу",
        "6": "Найти книгу",
        "0": "Выход"
    }

    # Dispatch Table: диспетчеризация вызова функций через словарь вместо if/elif
    actions = {
        "1": book_list_view,
        "2": handle_add_book,
        "3": handle_remove_book,
        "4": handle_issue_book,
        "5": handle_return_book,
        "6": handle_find_book
    }

    while True:
        print("\n--- Главное меню ---")
        for key, title in menu_titles.items():
            print(f"{key}. {title}")

        choice = input("Выберите действие: ").strip()

        if choice == "0":
            print("До свидания!")
            break

        action = actions.get(choice)
        if action:
            action(library)
        else:
            print("Некорректный ввод, попробуйте снова.")


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
