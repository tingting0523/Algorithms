'''
插入排序 (Insertion Sort) 是一种简单直观的排序算法，通常用于小规模数据集的排序。其核心思想是通过逐步构建有序序列，将每个元素插入到前面已经排序的部分中，直到整个数组排序完成。
'''

def insertionSort(arr):
    # 遍历从第二个元素开始（下标为1），因为第一个元素默认已排序
    for i in range(1, len(arr)):
        key = arr[i]  # 当前需要插入的元素
        j = i - 1  # key前面已排序部分的最后一个元素的索引
        
        # 将key与之前已经排好序的部分元素进行比较，如果比key大，则向后移动
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # 将元素向后移动
            j -= 1
        
        arr[j + 1] = key  # 找到合适位置插入key
        
        # 输出每次插入后的数组状态
        print(f"Step {i}: {arr}")
    
    return arr

# 示例使用
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)
sorted_arr = insertionSort(arr)
print("Sorted array:", sorted_arr)
