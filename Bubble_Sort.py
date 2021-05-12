def Bubble_Sort(array):
    j = 0
    n = len(array) -1
    for j in range(n):
        swapped = False
        for i in range(n-j):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                swapped = True
        if not swapped:
            break
    return array
print(Bubble_Sort([8,4,6,1,2,3,7,9,5]))
print(Bubble_Sort([1,2,3,4,5]))