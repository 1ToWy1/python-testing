with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Первая строка текста.\n")
    f.write("Вторая строка текста.\n")
    f.write("Третья строка текста.\n")

with open("data.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")

with open("data.txt", "a", encoding="utf-8") as f:
    f.write("Четвертая строка (добавлена).\n")
    f.write("Пятая строка (добавлена).\n")

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")

with open("data.txt", "rb") as src, open("data_copy.txt", "wb") as dst:
    dst.write(src.read())