number_to_word = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five"
}

def get_word(number: int) -> str:
    return number_to_word.get(number, "Ошибка: число должно быть от 1 до 5")

def main():
    try:
        number = int(input("Введите число от 1 до 5: "))
        print(f"Соответствующее слово: {get_word(number)}")
    except ValueError:
        print("Ошибка: введите целое число")

if __name__ == "__main__":
    main()
