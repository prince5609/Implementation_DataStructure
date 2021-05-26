def swap(a, b, array):
    if a != b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp


def partition(array, start, end):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while pivot < array[end]:
            end -= 1
        if start < end:
            swap(start, end, array)
    swap(pivot_index, end, array)
    return end


def quick_sort(array, start, end):
    if start < end:
        pi = partition(array, start, end)
        quick_sort(array, start, pi - 1)
        quick_sort(array, pi + 1, end)
    return array


data = [11, 9, 2, 7, 29, 15, 28]
data2 = [55, 33, 9, 41, 6, 1, 7, 2, 5, 879, 5, 5, 4, 85, 5646, 2585, 5564]
print(quick_sort(data, 0, len(data) - 1))
print(quick_sort(data2, 0, len(data2) - 1))
