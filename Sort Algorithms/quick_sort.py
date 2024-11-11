def quick_sort(arr, depth=0):
    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choosing the last element as the pivot
        pivot = arr[-1]
        # Elements less than the pivot
        left = [x for x in arr[:-1] if x <= pivot]
        # Elements greater than the pivot
        right = [x for x in arr[:-1] if x > pivot]

        # Print the array at the current depth level of recursion
        print(f"Depth {depth}: {arr}, Pivot: {pivot}")

        # Recursively sort left and right, then combine
        return quick_sort(left, depth + 1) + [pivot] + quick_sort(right, depth + 1)

# Example array
arr = [9, 7, 5, 11, 12]

# Sorting the array using Quick Sort
sorted_arr = quick_sort(arr)

# Print the final result
print("Sorted array:", sorted_arr)
