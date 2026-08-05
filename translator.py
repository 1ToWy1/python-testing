number_to_word = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five"
}

try:
    number = int(input("Введите число от 1 до 5: "))
except ValueError:
    print("Ошибка: введите целое число")
    exit()

if 1 <= number <= 5:
    print(f"Соответствующее слово: {number_to_word[number]}")
else:
    print("Ошибка: число должно быть от 1 до 5")
