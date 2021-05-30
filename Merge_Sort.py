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
        if a[i] <= b[j]:
            data_list[k] = a[i]
            i += 1
        else:
            data_list[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        data_list[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        data_list[k] = b[j]
        j += 1
        k += 1


if __name__ == "__main__":
    print(merge_sort([55, 33, 9, 41, 6, 1, 7, 2, 5, 879, 5, 5, 4, 85, 5646, 2585, 5564]))
    print(merge_sort([21, 38, 29, 17, 4, 25, 11, 29, 32, 9]))
    print(merge_sort([18, 14, 7, 25, 3, 29, 20, 30, 12]))
