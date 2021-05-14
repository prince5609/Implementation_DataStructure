def shell_sort(array):
    n = len(array)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            anchor = array[i]
            j = i
            while j >= gap and array[j-gap] > anchor:
                array[j] = array[j-gap]
                j -= gap
                array[j] = anchor
        gap = gap//2
    return array
print(shell_sort([21,38,29,17,4,25,11,32,9]))
print(shell_sort([18,14,7,25,3,29,20,30,12]))
print(shell_sort([1,2,3,4,5,-6]))



