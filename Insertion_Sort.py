def swap(a, b, array):
    if a != b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp
def insertion_sort(array):
    for i in range(1,len(array)):
        for j in range(0,i-1):
            swapped = False
            if array[i] < array[j]:
                swap(i,j,array)
                swapped = True
    return array
print(insertion_sort([21,29,38,17,4,25,11,32,9]))






