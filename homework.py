try:
    first_numder = int(input())
    second_numder = int(input())
    result = first_numder / second_numder
except ValueError:
    print("Ошибка: пользователь ввел нечисловое значение")
except ZeroDivisionError:
    print("Ошибка:второе число равно нулю")
else:
    print(result)
finally:
    print("сообщение о завершении работы программы")

