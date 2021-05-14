def selection_sort(array):
    i = 0
    while i <= len(array)-2:
        m = array.index(min(array[i+1:len(array)]))
        if array[i] > array[m]:
            temp = array[i]
            array[i] = array[m]
            array[m] = temp
        i += 1
    return array
print(selection_sort([21,38,29,17,4,25,11,32,9]))
print(selection_sort([1,0]))
print(selection_sort([1,2,3,4,5,6,7,8,9]))