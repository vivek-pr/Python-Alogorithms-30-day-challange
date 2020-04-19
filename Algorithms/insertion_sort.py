

def insertion_sort(input_list):
    cursor_location = 0
    list_len = len(input_list)
    loop_count = 0
    while cursor_location < list_len:
        for i in range(cursor_location, 0, -1):
            if input_list[i-1] > input_list[i]:
                input_list[i-1], input_list[i] = input_list[i], input_list[i-1]
            else:
                break
            loop_count += 1
        cursor_location += 1
    print(loop_count)
    return input_list

print(insertion_sort([12,-1, -2, -2, -3, 11, 11,9, 3, -1]))