while True:
    try:
        number = int(input("Введите целое положительное число: "))
        if number > 0:
            break
        else:
            print("Ошибка: число должно быть положительным (больше 0). Попробуйте снова.")
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте снова.")

print(f"Обратный отсчёт от {number} до 0:")
while number >= 0:
    print(number)
    number -= 1
