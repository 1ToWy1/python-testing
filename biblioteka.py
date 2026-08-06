def book_list_view(library):
    if not library:
        print("Библиотека пуста")
    else:
        for book in library.keys():
            print(book)


library = {
    "Мастер и Маргарита": {
        "автор": "Михаил Булгаков",
        "год издания": 1967,
        "наличие": "в наличии"
    },
    "Преступление и наказание": {
        "автор": "Федор Достоевский",
        "год издания": 1866,
        "наличие": "выдана"
    }
}

book_list_view(library)
