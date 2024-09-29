'''
selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest( or largest) element from the unsorted portion of the list and moving it to the sorted portion.
选择排序是一种简单而有效的排序算法，其工作方式是反复从列表的未排序部分中选择最小（或最大）元素并将其移动到已排序部分。
第一个元素不断地跟后面的所有元素比，将找到的最小元素与未排序部分的第一个元素进行交换
'''
import random

# Sorts arrat a[0..n-1] using Bogo sort
def selectionSort(a):
    n = len(a)
    # Traverse through all array elements
    for i in range(n):
       #Find the minimum element in remaining unsorted array 在剩余的未排序数组中查找最小元素
       min_idx = i
       for j in range(i+1,n):
          if arr[j]<arr[min_idx]:
             min_idx=j

       #Swap the found minimum element with the first element of the unsorted part 将找到的最小元素与未排序部分的第一个元素进行交换
       arr[i],arr[min_idx]=arr[min_idx],arr[i]

       #print the arrat after each eteration of selection sort
       print("Ater iteration",i+1,":",arr)
    return arr

# Drive code to test above
arr=[64,25,12,6,22,11]
print("Original array:", arr)
sorted_arr = selectionSort(arr)
print("Sorted array:", arr)
