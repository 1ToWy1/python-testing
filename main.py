try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 + num2
    print(result)
except ValueError:
    print("Ошибка: Введено не число")

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 - num2
    print(result)
except ValueError:
    print("Ошибка: Введено не число")

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 * num2
    print(result)
except ValueError:
    print("Ошибка: Введено не число")

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Ошибка: Деление на ноль недопустимо")
except ValueError:
    print("Ошибка: Введено не число")
