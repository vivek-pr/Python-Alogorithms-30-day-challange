"""
Binary search: Serach a sorted array by dividing into half and then comparing the searched value.
"""

def binary_serach(sorted_list, searched):
    index = -1
    list_len = len(sorted_list)
    mid = list_len//2
    while sorted_list and mid > 0:
        if sorted_list[mid] < searched:
            mid += mid//2
            list_len = sorted_list[mid:list_len]
        elif sorted_list[mid] > searched:
            mid = mid//2
            list_len = sorted_list[0:mid]
        else:
            index = mid
            break

    return index

bin_value = binary_serach([1,2,3,4,5,6], 5)

print(bin_value)