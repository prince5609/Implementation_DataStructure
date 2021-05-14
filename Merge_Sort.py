def merge_sort(array):
    if len(array) <= 1:
        return
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_list(left, right, array)

def merge_two_sorted_list(a, b, array):
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            array[k] = b[j]
            j += 1
        elif a[i] < b[j]:
            array[k] = a[i]
            i += 1
        k += 1
    while i < len(a):
        array[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        array[k] = b[j]
        j += 1
        k += 1
array = [18,14,7,25,3,29,20,30,12]
merge_sort(array)
print(array)




