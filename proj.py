def max_number(a, b):
    if a > b:
        return a
    return b

def empty_function():
    pass

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def test_max_number():
    assert max_number(5, 3) == 5
    assert max_number(3, 5) == 5
    assert max_number(-1, -5) == -1
    assert max_number(0, 0) == 0
    assert max_number(10, 10) == 10
    assert max_number(-10, 5) == 5
    assert max_number(2.5, 1.5) == 2.5
    print("Все тесты пройдены!")

test_max_number()

print(list(even_numbers(10)))