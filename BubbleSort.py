def bubbleSort(arr):
    n=len(arr)
    #Traverse through all array elements
    for i in range(n):
        #Last i elements are already in place
        for j in range(0,n-i-1):
            #Traverse the array from 0 to n-i-1
            #Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            #Print the array after each seap
            print("Step:",arr)
        print("After pass",i+1,":",arr)
        print()
    return arr 

#Drive code to test above
arr=[64,34,25,12,22,11,90]
print("Original array:",arr)
sorted_arr=bubbleSort(arr)
print("Sorted array", sorted_arr)
