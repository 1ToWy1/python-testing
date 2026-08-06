def count_unique_elements(lst):
    return len(set(lst))


my_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5, 8, 9, 1]
result = count_unique_elements(my_list)
print(f"Количество уникальных элементов: {result}")
