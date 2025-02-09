import random

def partition(arr, left, right):
    pivot = arr[right]  # Choose last element as pivot
    i = left  # Pointer for smaller elements
    
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
            i += 1
    
    arr[i], arr[right] = arr[right], arr[i]  # Swap pivot into correct position
    return i  # Return pivot index

def randomized_quickselect(arr, left, right, k):
    if left == right:
        return arr[left]
    
    pivot_index = random.randint(left, right)  # Pick random pivot
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # Move pivot to end
    
    partition_index = partition(arr, left, right)  # Partition the array
    
    if partition_index == k:  # If pivot is the k-th smallest element
        return arr[partition_index]
    elif partition_index > k:  # Search left partition
        return randomized_quickselect(arr, left, partition_index - 1, k)
    else:  # Search right partition
        return randomized_quickselect(arr, partition_index + 1, right, k)

def quickselect(arr, k):
    return randomized_quickselect(arr, 0, len(arr) - 1, k - 1)

# Example usage:
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}rd smallest element:", quickselect(arr, k))
