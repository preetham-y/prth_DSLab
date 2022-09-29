#DATA STRUCTURES UNIT 1 TASKS
#SORTING & SEARCHING

#Linear Search
my_List = [10, 35, 42, 51, 62]

pivot = int(input("Enter a number:"))


for i in my_List:
    if pivot==i:
        flag = 1
        break
    else:
        flag = 0
    
if flag == 1:
    print("Element Found")
else:
    print("Element Not Found")

#Binary Search
def binarySearch(array, x, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

#Selection Sort
def sort(nums):
  for i in range(5):
    minpos=i
    for j in range(i,6):
      if nums[j]<nums[minpos]:
        minpos=j
    temp=nums[i]
    nums[i]=nums[minpos]
    nums[minpos]=temp


    print(nums)
nums=[100,-1,5,78,4,2]
sort(nums)

print(nums)

#Insertion Sort
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
      
        array[j + 1] = key


data = [55,43,-22,0,300,1]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

#Quick Sort
def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)
data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)

#Bubble Sort
def bubblesort(array):
  for i in range(len(array)):
    for j in range(0,len(array)-1-1):
      if array[j]>array[j+1]:
        array[j],array[j+1]=array[j+1],array[j]
data=[-1,7,10,0,8,70]
bubblesort(data)
print(data)

#Merge Sort
def merge_sort(arr):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]
        merge_sort(left_arr) 
        merge_sort(right_arr)

        #Merging
        i=0#left most element in left array
        j=0#left most element in right array
        k=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<=right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        while i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1

arr = [3,5,4,7,6,1,2,0]
merge_sort(arr)
print(arr)