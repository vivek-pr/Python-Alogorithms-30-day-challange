import random


def quick_sort(unordered_list):
    list_len = len(unordered_list)
    if list_len < 1:
        return unordered_list
    else:
        # To avoid worst case.
        random_pivot_index = random.randint(0, list_len)
        pivot = unordered_list[random_pivot_index]

        left_sort = [item for item in unordered_list if item < pivot]
        right_sort = [item for item in unordered_list if item > pivot]
        return quick_sort(left_sort) + [pivot] + quick_sort(right_sort)


unordered_list = [11,2,3,0,7,9,12,5]
print(quick_sort(unordered_list))

