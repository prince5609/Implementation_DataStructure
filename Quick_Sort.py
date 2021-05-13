array = [11, 9, 2, 7, 29, 15, 28]
class Quick_Sort:
    def swap(self, a, b, array):
        if a!=b:
            temp = array[a]
            array[a] = array[b]
            array[b] = temp


    def partition(self,array,start,end):
        pivot_index = start
        pivot = array[pivot_index]

        while start < end:
            while start < len(array) and array[start] <= pivot:
                start += 1
            while pivot < array[end]:
                end -= 1
            if start < end:
                self.swap(start, end, array)
        self.swap(pivot_index, end, array)
        return end


    def quick_sort(self, array, start, end):
        if start < end:
            pi = self.partition(array, start, end)
            self.quick_sort(array, start, pi-1)
            self.quick_sort(array, pi+1, end)
        return array


obj = Quick_Sort()
print(obj.quick_sort(array, 0, len(array)-1))

