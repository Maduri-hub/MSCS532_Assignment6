def median_of_medians(arr, left, right):
    if right - left + 1 <= 5:  # Base case: if small, sort & return median
        return sorted(arr[left:right+1])[(right - left) // 2]

    medians = []
    for i in range(left, right + 1, 5):  # Divide into groups of 5
        sub_right = min(i + 4, right)
        sorted_sublist = sorted(arr[i:sub_right + 1])  # Sort small group
        medians.append(sorted_sublist[(sub_right - i) // 2])  # Get median

    return median_of_medians(medians, 0, len(medians) - 1)  # Recursively find median

def deterministic_partition(arr, left, right, pivot):
    pivot_index = arr.index(pivot)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # Move pivot to end
    return partition(arr, left, right)

def deterministic_select(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot = median_of_medians(arr, left, right)  # Get good pivot
    partition_index = deterministic_partition(arr, left, right, pivot)  # Partition

    if partition_index == k:
        return arr[partition_index]
    elif partition_index > k:
        return deterministic_select(arr, left, partition_index - 1, k)
    else:
        return deterministic_select(arr, partition_index + 1, right, k)

def median_of_medians_select(arr, k):
    return deterministic_select(arr, 0, len(arr) - 1, k - 1)

# Example usage:
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}rd smallest element using Median of Medians:", median_of_medians_select(arr, k))
