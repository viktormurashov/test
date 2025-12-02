a = [7, 14, 1, 88, 32, 4, 65, 76]
n = len(a)

def bubble_sort(arr):
  for i in range(n-1):
    for j in range(n-i-1):
      if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]

print(a)

def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]
  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)
  return merge(sortedLeft, sortedRight)
def merge(left, right):
  result = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result.extend(left[i:])
  result.extend(right[j:])
  return result
a = [6, 54, -10, 7, 14.1, 22, -13]
b = mergeSort(a)
print(b)

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
     if array[j] <= pivot:
       i += 1
       array[i], array[j] = array[j], array[i]
  array[i+1], array[high] = array[high], array[i+1]
  return i+1
def quicksort(array, low = 0, high = None):
  if high is None:
    high = len(array) - 1
  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index - 1)
    quicksort(array, pivot_index + 1, high)
a = [5, 56, 87, 32, 4, 19, 63, 43]
quicksort(a)
print(a)