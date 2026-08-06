def get_positive_int():
    while True:
        try:
            number = int(input("Введите целое положительное число: "))
            if number > 0:
                return number
            print("Ошибка: число должно быть положительным (больше 0). Попробуйте снова.")
        except ValueError:
            print("Ошибка: нужно ввести целое число. Попробуйте снова.")


def countdown(start):
    print(f"Обратный отсчёт от {start} до 0:")
    for i in range(start, -1, -1):
        print(i)


def main():
    number = get_positive_int()
    countdown(number)


if __name__ == "__main__":
    main()
