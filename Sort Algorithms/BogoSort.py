'''
bogoSort（又称“猴子排序”或“随机排序”） 
是一种极其低效的排序算法，它通过不断随机打乱数组的顺序，直到数组变为有序为止。
shuffle(a) 的作用就是随机打乱数组的顺序
is_sorted(a) 则检查数组是否已经排序好
'''

import random

# To check if array is sorted or not
def is_sorted(a):
   n=len(a)
   for i in range(0, n-1):
      if a[i] > a[i+1]:
         return False
   return True

# To generates a permutation of the array 生成数组的排列
def shuffle(a):
   n=len(a)
   for i in range(n):
      r = random.randint(0, n-1)
      a[i], a[r] = a[r], a[i]

# Sorts arrat a[0..n-1] using Bogo sort
def bogoSort(a):
    n = len(a)
    while not is_sorted(a):
     shuffle(a)    #将数组或列表 a 的元素随机重新排列，打乱其顺序
     print("Current arrat values", a)

# Drive code to test above
a=[3,2,4]
bogoSort(a)
print("Sorted array:")
print("".join(str(x) for x in a))  #将列表 a 中的所有元素转换为字符串并连接成一个整体字符串，然后打印出来
