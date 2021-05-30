def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        anchor = array[i]
        while j >= 0 and anchor < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = anchor
    return array


print(insertion_sort([8, 4, 6, 1, 2, 3, 7, 6, 9, 5]))
print(insertion_sort([21, 29, 38, 17, 4, 25, 11, 32, 9]))
