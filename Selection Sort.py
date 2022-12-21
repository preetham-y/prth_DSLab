#Selection Sort
def sort(array, size):
    
    for i in range(size):
        min_index = i
 
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])
 
arr = [45,24,56,2,3,4]
size = len(arr)
sort(arr, size)
print(arr)
