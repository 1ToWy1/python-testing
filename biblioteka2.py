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


def book_list_view(lib):
    if not lib:
        print("Библиотека пуста")
    else:
        for book in lib.keys():
            print(book)


def add_book(title, author, year):
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

    if title in library:
        print(f"Книга '{title}' уже существует в библиотеке.")
        choice = input("Хотите обновить информацию? (да/нет): ").lower()

        if choice == "да":
            library[title] = {
                "автор": author,
                "год издания": year,
                "наличие": None
            }
            print(f"Информация о книге '{title}' обновлена")
        else:
            print("Операция отменена")
    else:
        library[title] = {
            "автор": author,
            "год издания": year,
            "наличие": None
        }
        print(f"Книга '{title}' успешно добавлена")


book_list_view(library)
