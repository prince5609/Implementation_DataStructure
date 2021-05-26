def selection(array):
    for i in range(len(array) - 1):
        minimum = min(array[i + 1:len(array)])
        if array[i] > minimum:
            index = array[i + 1:len(array)].index(minimum)
            array[i], array[index + i + 1] = array[index + i + 1], array[i]
        elif array[i] == minimum:
            index = array[i + 1:len(array)].index(minimum)
            array[i + 1], array[index + i + 1] = array[index + i + 1], array[i + 1]
    return array


print(selection([21, 38, 29, 17, 4, 25, 11, 29, 32, 9]))
print(selection([1, 0]))
print(selection([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(selection([55, 33, 9, 41, 6, 1, 7, 2, 5, 879, 5, 5, 4, 85, 5646, 2585, 5564]))
print(selection([5, 5, 5, 5, 5, 5, 5, 5, 5]))
