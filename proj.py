def max_number(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами (int или float)")
    if a > b:
        return a
    return b


def empty_function():
    pass


def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


def test_max_number():
    assert max_number(5, 3) == 5, "Ошибка: 5 > 3, должно быть 5"
    assert max_number(3, 5) == 5, "Ошибка: 5 > 3, должно быть 5"
    assert max_number(-1, -5) == -1, "Ошибка: -1 > -5, должно быть -1"
    assert max_number(0, 0) == 0, "Ошибка: равные числа 0 и 0, должно быть 0"
    assert max_number(-10, 5) == 5, "Ошибка: 5 > -10, должно быть 5"
    assert max_number(2.5, 1.5) == 2.5, "Ошибка: 2.5 > 1.5, должно быть 2.5"
    print("Все тесты пройдены!")


test_max_number()
print(list(even_numbers(10)))
