def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_two_sorted_list(left, right)

def merge_two_sorted_list(a, b):
    sorted_arr = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            sorted_arr.append(b[j])
            j += 1
        elif a[i] < b[j]:
            sorted_arr.append(a[i])
            i += 1
    while i < len(a):
        sorted_arr.append(a[i])
        i += 1
    while j < len(b):
        sorted_arr.append(b[j])
        j += 1
    return sorted_arr

print(merge_sort([18,14,7,25,3,29,20,30,12]))




