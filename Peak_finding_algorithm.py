import numpy as np

linear_count=0
divide_conquer_count=0

def find_peak_linear(arr):
    global linear_count
    linear_count=0
    n=len(arr)
    for i in range(n):
        linear_count += 1 # Counting the comparison
        if(i==0 or arr[i]>=arr[i-1]) and (i==n-1 or arr[i]>=arr[i+1]):
            return arr[i]
    return None

def find_peak_divide_conquer(arr,low,high):
    global divide_conquer_count
    

    def helper(arr,low,high):  # low represent the start index of the array. high represent the end index of the array.
        global divide_conquer_count
        mid = (low+high)//2
        divide_conquer_count += 1 #Counting the comparison
        n=len(arr)
        if(mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
            return arr[mid]
        elif mid>0 and arr[mid-1]>arr[mid]:
            return helper(arr,low,mid-1)
        else:
            return helper(arr,mid+1,high)
    return helper(arr,low,high)

#example array
arr1 = [1,3,20,4,1]
arr2 = [1,3,5,7,9,11,13,15]
arr3 = [10,20,15,2,23,90,67]
arr4 = [1,9,2,3,5,6,8]

#Finding peaks and counting calculations
peak_linear_1=find_peak_linear(arr1)
peak_divide_conquer_1 = find_peak_divide_conquer(arr1,0,len(arr1)-1)
print(f"Peak in arr1(linear):{peak_linear_1},calculations:{linear_count}")
print(f"Peak in arr1(divide-conquer):{peak_divide_conquer_1},calculations:{divide_conquer_count}")
print("")

peak_linear_2=find_peak_linear(arr2)
peak_divide_conquer_2 = find_peak_divide_conquer(arr2,0,len(arr2)-1)
print(f"Peak in arr2(linear):{peak_linear_2},calculations:{linear_count}")
print(f"Peak in arr2(divide-conquer):{peak_divide_conquer_2},calculations:{divide_conquer_count}")
print("")

peak_linear_3=find_peak_linear(arr3)
peak_divide_conquer_3 = find_peak_divide_conquer(arr3,0,len(arr3)-1)
print(f"Peak in arr3(linear):{peak_linear_3},calculations:{linear_count}")
print(f"Peak in arr3(divide-conquer):{peak_divide_conquer_3},calculations:{divide_conquer_count}")
print("")

peak_linear_4=find_peak_linear(arr4)
peak_divide_conquer_4 = find_peak_divide_conquer(arr4,0,len(arr4)-1)
print(f"Peak in arr4(linear):{peak_linear_4},calculations:{linear_count}")
print(f"Peak in arr4(divide-conquer):{peak_divide_conquer_4},calculations:{divide_conquer_count}")
print("")