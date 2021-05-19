def count_sort(array):
    maximum = max(array)
    count_array = [0] * (maximum + 1)
    while maximum >= min(array):
        count = array.count(maximum)
        count_array[maximum] = count
        maximum -= 1
    for i in range(len(count_array) - 1):
        count_array[i + 1] = count_array[i + 1] + count_array[i]
    result_array = [0] * len(array)
    for j in range(len(array)):
        value = count_array[array[j]]
        result_array[value - 1] = array[j]
        count_array[array[j]] = count_array[array[j]] - 1
    return result_array


print(count_sort([2, 1, 2, 6, 0, 4, 3, 3]))
print(count_sort([2, 4, 9, 6, 7, 9, 3, 4, 8, 1, 5]))
