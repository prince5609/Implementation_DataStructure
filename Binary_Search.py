def binary_search(array, target):
    start = 0
    end = len(array) - 1
    mid = (end - start) // 2
    while end > start:
        if target == array[start]:
            return start
        elif target == array[end]:
            return end
        elif target == array[mid]:
            return mid
        elif target > array[mid]:
            start = mid + 1
            mid = ((end - start) // 2) + start
        elif target < array[mid]:
            end = mid - 1
            mid = ((end - start) // 2) + start


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
print(binary_search([1, 2, 3], 0))
print(binary_search([10, 20, 30, 40, 50, 100], 10))
