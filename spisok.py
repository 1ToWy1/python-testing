def swap_first_and_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst


fruits = ["яблоко", "банан", "груша", "апельсин", "киви"]
result = swap_first_and_last(fruits)

print(result)
