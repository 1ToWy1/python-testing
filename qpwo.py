def calculate_sum_even():
    return sum(range(2, 101, 2))


def get_odd_squares():
    return [i ** 2 for i in range(1, 11, 2)]


def collect_numbers():
    numbers = []
    print("Введите числа. Для завершения введите отрицательное число.")

    while True:
        try:
            user_input = float(input("Введите число: "))

            if user_input < 0:
                print("Введено отрицательное число. Программа завершена.")
                break

            numbers.append(user_input)
            print(f"Введено чисел: {len(numbers)}")

        except ValueError:
            print("Ошибка: нужно ввести число. Попробуйте снова.")

    return numbers


def main():
    sum_even = calculate_sum_even()
    print(f"Сумма чётных чисел от 1 до 100: {sum_even}")

    odd_squares = get_odd_squares()
    print(f"Квадраты нечётных чисел от 1 до 10: {odd_squares}")

    numbers = collect_numbers()
    count = len(numbers)

    print(f"\nВсего введено чисел (без отрицательного): {count}")
    if numbers:
        total_sum = sum(numbers)
        avg = total_sum / count
        print(f"Введённые числа: {numbers}")
        print(f"Сумма чисел: {total_sum}")
        print(f"Среднее арифметическое: {avg:.2f}")


if __name__ == "__main__":
    main()
