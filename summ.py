def sum_two_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Оба аргумента должны быть списками.")

    for item in list1 + list2:
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"Все элементы списков должны быть числами. Найден элемент: {item} ({type(item).__name__})"
            )

    result = []
    min_length = min(len(list1), len(list2))

    for i in range(min_length):
        result.append(list1[i] + list2[i])

    return result


numbers1 = [1, 5, 8, 10, 3]
numbers2 = [4, 2, 1]

result_list = sum_two_lists(numbers1, numbers2)
print("Результат сложения:", result_list)
