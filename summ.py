def sum_two_lists(list1, list2):
    min_len = min(len(list1), len(list2))

    result = [list1[i] + list2[i] for i in range(min_len)]

    if len(list1) > len(list2):
        result.extend(list1[min_len:])
    else:
        result.extend(list2[min_len:])

    return result


numbers_1 = [1, 5, 8, 10, 3]
numbers_2 = [4, 2, 1]

result_list = sum_two_lists(numbers_1, numbers_2)
print("Результат сложения:", result_list)
