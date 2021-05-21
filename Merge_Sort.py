def merge_sort(data_list):
    if len(data_list) <= 1:
        return
    mid = len(data_list) // 2
    left = data_list[:mid]
    right = data_list[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_list(left, right, data_list)
    return data_list


def merge_two_sorted_list(a, b, data_list):
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            data_list[k] = b[j]
            j += 1
        elif a[i] < b[j]:
            data_list[k] = a[i]
            i += 1
        k += 1
    while i < len(a):
        data_list[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        data_list[k] = b[j]
        j += 1
        k += 1


array = [18, 14, 7, 25, 3, 29, 20, 30, 12]
print(merge_sort(array))
