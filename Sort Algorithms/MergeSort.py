'''
Merge Sort 是一种基于“分治法”思想的高效排序算法。它通过将数组递归地拆分成较小的部分进行排序，最终通过合并这些已排序的子部分来完成整个数组的排序。

'''

def mergeSort(arr):
    if len(arr) > 1:
        # 找出数组的中点
        mid = len(arr) // 2
        
        # 将数组分成两部分
        L = arr[:mid]
        R = arr[mid:]
        
        # 对左右两部分分别进行递归归并排序
        mergeSort(L)
        mergeSort(R)
        
        i = j = k = 0
        
        # 合并两个子数组
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # 检查左半部分是否有剩余元素
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        # 检查右半部分是否有剩余元素
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# 示例使用
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
mergeSort(arr)
print("Sorted array:", arr)
