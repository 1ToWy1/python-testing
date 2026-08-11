def sum_two_lists(list1, list2):
    result = []
    max_length = max(len(list1), len(list2))

    for i in range(max_length):
        val1 = list1[i] if i < len(list1) else 0
        val2 = list2[i] if i < len(list2) else 0
        result.append(val1 + val2)

    return result


numbers_1 = [1, 5, 8, 10, 3]
numbers_2 = [4, 2, 1]

result_list = sum_two_lists(numbers_1, numbers_2)
print("Результат сложения:", result_list)
