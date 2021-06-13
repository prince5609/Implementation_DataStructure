def binary_search(array, target):
    if target not in array:
        return None
    start = 0
    end = len(array) - 1
    mid = (end + start) >> 1
    while array[mid] != target:
        if target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (end + start) >> 1
    return mid


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
print(binary_search([10, 20, 30, 40, 50, 100], 10))
print(binary_search([5, 8, 12, 26, 38, 49, 65, 98, 100], 38))
print(binary_search([5, 8, 12, 26, 38, 49, 65, 98, 100], 1000))
