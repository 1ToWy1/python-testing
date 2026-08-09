def book_list_view(lib):
    if not lib:
        print("Библиотека пуста")
        return

    for book in lib.keys():
        print(book)


def add_book(lib, title, author, year):
    if not title or not title.strip():
        print("Ошибка: Название книги не может быть пустым")
        return

    if not author or not author.strip():
        print("Ошибка: Имя автора не может быть пустым")
        return

    try:
        year = int(year)
    except ValueError:
        print("Ошибка: Год издания должен быть числом")
        return

    if year < 0 or year > 2026:
        print("Ошибка: Некорректный год издания")
        return

    if title in lib:
        print(f"Книга '{title}' уже существует в библиотеке.")
        choice = input("Хотите обновить информацию? (да/нет): ").lower()

        if choice == "да":
            lib[title] = {
                "автор": author,
                "год издания": year,
                "наличие": None
            }
            print(f"Информация о книге '{title}' обновлена")
            return

        print("Операция отменена")
        return

    lib[title] = {
        "автор": author,
        "год издания": year,
        "наличие": None
    }
    print(f"Книга '{title}' успешно добавлена")


def remove_book(lib, title):
    if not title or not title.strip():
        print("Ошибка: Название книги не может быть пустым")
        return

    title = title.strip()

    if title not in lib:
        print(f"Ошибка: Книга '{title}' не найдена в библиотеке")
        return

    del lib[title]
    print(f"Книга '{title}' успешно удалена")


def issue_book(lib, title):
    if not title or not title.strip():
        print("Ошибка: Название книги не может быть пустым")
        return

    title = title.strip()

    if title not in lib:
        print(f"Ошибка: Книга '{title}' не найдена в библиотеке")
        return

    lib[title]["наличие"] = False
    print(f"Книга '{title}' выдана")


def return_book(lib, title):
    if not title or not title.strip():
        print("Ошибка: Название книги не может быть пустым")
        return

    title = title.strip()

    if title not in lib:
        print(f"Ошибка: Книга '{title}' не найдена в библиотеке")
        return

    lib[title]["наличие"] = True
    print(f"Книга '{title}' возвращена в библиотеку")


def find_book(lib, title):
    if not title or not title.strip():
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


def main_menu():
    menu_options = {
        "1": "Просмотреть список книг",
        "2": "Добавить книгу",
        "3": "Удалить книгу",
        "4": "Выдать книгу",
        "5": "Вернуть книгу",
        "6": "Найти книгу",
        "0": "Выход"
    }

    while True:
        print("\n--- Главное меню ---")
        for key, value in menu_options.items():
            print(f"{key}. {value}")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            book_list_view(library)
        elif choice == "2":
            t = input("Введите название книги: ")
            a = input("Введите автора: ")
            y = input("Введите год издания: ")
            add_book(library, t, a, y)
        elif choice == "3":
            t = input("Введите название книги для удаления: ")
            remove_book(library, t)
        elif choice == "4":
            t = input("Введите название книги для выдачи: ")
            issue_book(library, t)
        elif choice == "5":
            t = input("Введите название книги для возврата: ")
            return_book(library, t)
        elif choice == "6":
            t = input("Введите название книги для поиска: ")
            find_book(library, t)
        elif choice == "0":
            print("До свидания!")
            break
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
