import random

# Sorts arrat a[0..n-1] using Bogo sort
def bogoSort(a):
    n = len(a)
    while not is_sorted(a):
     shuffle(a)
     print("Current arrat values", a)

# To check if array is sorted or not
def is_sorted(a):
   n=len(a)
   for i in range(0, n-1):
      if a[i] > a[i+1]:
         return False
   return True

# To generates a permutation of the array
def shuffle(a):
   n=len(a)
   for i in range(n):
      r = random.randint(0, n-1)
      a[i], a[r] = a[r], a[i]

# Drive code to test above
a=[3,2,4]
bogoSort(a)
print("Sorted array:")
print("".join(str(x) for x in a))
