def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(min_index+1,len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i],array[min_index] = array[min_index],array[i]
    return array

print(selection_sort([21,38,29,17,4,25,11,32,9]))
print(selection_sort([1,0]))
print(selection_sort([1,2,3,4,5,6,7,8,9]))
print(selection_sort([55,33,9,41,6,1,7,2,5,879,5,5,4,85,5646,2585,5564]))
print(selection_sort([5,5,5,5,5,5,5,5,5]))