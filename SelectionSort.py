import random

# Sorts arrat a[0..n-1] using Bogo sort
def selectionSort(a):
    n = len(a)
    # Traverse through all array elements
    for i in range(n):
       #Find the minimum element in remaining unsorted array
       min_idx = i
       for j in range(i+1,n):
          if arr[j]<arr[min_idx]:
             min_idx=j

       #Swap the found minimum element with the first element of the unsorted part
       arr[i],arr[min_idx]=arr[min_idx],arr[i]

       #print the arrat after each eteration of selection sort
       print("Ater iteration",i+1,":",arr)
    return arr

# Drive code to test above
arr=[64,25,12,22,11]
print("Original array:", arr)
sorted_arr = selectionSort(arr)
print("Sorted array:", arr)
