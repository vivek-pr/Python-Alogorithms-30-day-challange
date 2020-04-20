"""
Your computer’s memory is like a giant set of drawers.
When you want to store multiple elements, use an array or a list.
With an array, all your elements are stored right next to each other.
With a list, elements are strewn all over, and one element stores the address of the next one.
Arrays allow fast reads.
Linked lists allow fast inserts and deletes.
All elements in the array should be the same type (all ints, all doubles, and so on).
"""


def selection_sort(unorderd_list):

    list_len = len(unorderd_list)
    i = 0
    while i < list_len:
        min_index = i
        for val in range(i, list_len):
            if unorderd_list[val] < unorderd_list[min_index]:
                min_index = val
        unorderd_list[i], unorderd_list[min_index] = unorderd_list[min_index], unorderd_list[i]
        i += 1
    return unorderd_list

order_list = selection_sort([12,3,2,0,19, -1])
print(order_list)