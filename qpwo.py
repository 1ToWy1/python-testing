sum_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i

print(f"Сумма чётных чисел от 1 до 100: {sum_even}")

sum_even = 0
for i in range(2, 101, 2):
    sum_even += i
# -------------------------------------------------------
odd_squares = [i ** 2 for i in range(1, 11) if i % 2 != 0]

print(f"Квадраты нечётных чисел от 1 до 10: {odd_squares}")

count = 0
# --------------------------------------------------------
numbers = []

print("Введите числа. Для завершения введите отрицательное число.")

while True:
    try:
        user_input = float(input("Введите число: "))

        if user_input < 0:
            print(f"Введено отрицательное число. Программа завершена.")
            break

        count += 1
        numbers.append(user_input)
        print(f"Введено чисел: {count}")

    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте снова.")

print(f"\nВсего введено чисел (без отрицательного): {count}")
if numbers:
    print(f"Введённые числа: {numbers}")
    print(f"Сумма чисел: {sum(numbers)}")
    print(f"Среднее арифметическое: {sum(numbers) / len(numbers):.2f}")
