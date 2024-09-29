'''
BubbleSort 冒泡排序
不断地把最大值放在最右侧

bubble sort compare the 1st element and 2nd element, then compare 2nd element and 3rd element.
selection sort compare the 1st element and 2nd element, then compare 1st element and 3rd element.

i 是外层循环的计数器，它表示当前正在进行第几轮冒泡排序（pass）
j 控制的是内层循环，用于在每轮冒泡中遍历还未排序的元素。内层循环的作用是比较并交换相邻的元素，确保每次迭代后最大的元素“冒泡”到数组的最后
每一轮冒泡操作都要让当前部分的最大值“冒泡”到最后，而每次冒泡后，最后的 i 个元素已经排好序了，不需要再比较。因此，j 的范围是从 0 到 n-i-1，即仅遍历尚未排序的部分。
'''

def bubbleSort(arr):
    n=len(arr)
    #Traverse through all array elements 遍历所有数组元素
    for i in range(n):    
        #Last i elements are already in place 最后 i 个元素已经到位
        for j in range(0,n-i-1):
            #Traverse the array from 0 to n-i-1    遍历数组从0到n-i-1
            #Swap if the element found is greater than the next element 如果找到的元素大于下一个元素，则交换
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            #Print the array after each seap
            print("Step:",arr)
        print("After pass",i+1,":",arr)
        print()
    return arr 

#Drive code to test above
arr=[64,34,25,12,22,11,90,4]
print("Original array:",arr)
sorted_arr=bubbleSort(arr)
print("Sorted array", sorted_arr)
