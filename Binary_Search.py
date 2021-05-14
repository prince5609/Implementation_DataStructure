def binary_search(array,x):
    start = 0
    end = len(array) - 1
    mid = (len(array) - start)//2
    while end > start:
        if x == array[start]:
            return start
        elif x == array[end]:
            return end
        elif x == array[mid]:
             return mid
        elif x > array[mid]:
            start = mid + 1
            mid = ((end - start)//2) + start
        elif x < array[mid]:
            end = mid - 1
            mid = ((end - start)//2) + start
print(binary_search([1,2,3,4,5,6,7,8,9],7))
print(binary_search([],0))
print(binary_search([10,20,30,40,50,100],10))

