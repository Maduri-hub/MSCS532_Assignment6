import time
import random

# Quickselect (Randomized Selection)
def partition(arr, left, right):
    pivot = arr[right]  # Choose last element as pivot
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def randomized_quickselect(arr, left, right, k):
    if left == right:
        return arr[left]
    
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    partition_index = partition(arr, left, right)

    if partition_index == k:
        return arr[partition_index]
    elif partition_index > k:
        return randomized_quickselect(arr, left, partition_index - 1, k)
    else:
        return randomized_quickselect(arr, partition_index + 1, right, k)

def quickselect(arr, k):
    return randomized_quickselect(arr, 0, len(arr) - 1, k - 1)

# Median of Medians (Deterministic Selection)
def median_of_medians(arr, left, right):
    if right - left + 1 <= 5:
        return sorted(arr[left:right+1])[(right - left) // 2]

    medians = []
    for i in range(left, right + 1, 5):
        sub_right = min(i + 4, right)
        sorted_sublist = sorted(arr[i:sub_right + 1])
        medians.append(sorted_sublist[(sub_right - i) // 2])

    return median_of_medians(medians, 0, len(medians) - 1)

def deterministic_partition(arr, left, right, pivot):
    pivot_index = arr.index(pivot)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    return partition(arr, left, right)

def deterministic_select(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot = median_of_medians(arr, left, right)
    partition_index = deterministic_partition(arr, left, right, pivot)

    if partition_index == k:
        return arr[partition_index]
    elif partition_index > k:
        return deterministic_select(arr, left, partition_index - 1, k)
    else:
        return deterministic_select(arr, partition_index + 1, right, k)

def median_of_medians_select(arr, k):
    return deterministic_select(arr, 0, len(arr) - 1, k - 1)

# Performance Test Function
def measure_time(selection_algorithm, arr, k):
    start = time.time()
    selection_algorithm(arr[:], k)  # Use a copy to avoid modifying the original
    end = time.time()
    return end - start

# Test Cases
sizes = [50, 500, 900]  # Different input sizes
distributions = {
    "Random": lambda n: random.sample(range(n * 10), n),
    "Sorted": lambda n: list(range(n)),
    "Reverse-Sorted": lambda n: list(range(n, 0, -1))
}

results = {}

for size in sizes:
    results[size] = {}
    for name, generator in distributions.items():
        arr = generator(size)
        k = size // 2  # Find the median
        
        time_quickselect = measure_time(quickselect, arr, k)
        time_median_of_medians = measure_time(median_of_medians_select, arr, k)
        
        results[size][name] = {
            "Quickselect": time_quickselect,
            "Median of Medians": time_median_of_medians
        }

for k in results:
    print(k, results[k])
    print()
# print(results)