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
        choice = input("Хотите обновить информацию? (да/нет): ").lower()
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
