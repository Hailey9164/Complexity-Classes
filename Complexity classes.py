# Complexity classes
print("Complexity Classes")

# O(1)
# runs in constant time
print("\nO(1): Constant Time")
print("Hello World")


# O(log n)
# runs in logarithmic time
# the numbers list is sorted, so we can use binary search to find the target number
# Each step cuts the search space in half, producing a logarithmic runtime.
print("\nO(log n): Binary Search")

# Binary search function
def binary_search(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1
    # Perform binary search
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers = [1, 2, 3, 4, 5]
print(f"Searching for 2 in {numbers}:")
print(f"Found at index: {binary_search(numbers, 2)}")


# O(n) 
# runs in linear time
# the algorithm iterates through the list once
print("\nO(n): for loop")
print("Iterating through the list:")
for i in range(len(numbers)):
    print(numbers[i], end=" ")
print()  # New line after the loop

# O(n log n)
# runs in linearithmic time
# Merge sort runs in O(n log n) because:
#   The list is repeatedly split in half → log n levels of recursion
#   Each level performs a merge that touches all n elements
#   Combining them gives:
#       O(n log n)
print("\nO(n log n): Merge Sort")

def merge_sort(arr):
    # Base case: arrays of size 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])     # sort left half
    right = merge_sort(arr[mid:])    # sort right half
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

numbers = [5, 1, 4, 2, 3]
print(f"Sorted {numbers}: {merge_sort(numbers)}")


# O(n^2) 
# runs in quadratic time
# the algorithm has nested loops, each running n times
print("\nO(n^2): Nested loops")
print("Adding each pair of numbers in the list:")
numbers = [1, 2, 3, 4, 5]
# first loop iterates through the list
for i in range(len(numbers)):
    # second loop iterates through the list again
    for j in range(len(numbers)):
        print(numbers[i] + numbers[j], end=" ")
    print()  # New line after each pair


# O(n^3), 
# runs in cubic time
# the algorithm has three nested loops, each running n times
print("\nO(n^3): Three nested loops")
print("Adding each triplet of numbers in the list:")
#  first loop iterates through the list
for i in range(len(numbers)):
    # second loop iterates through the list again
    for j in range(len(numbers)):
        # third loop iterates through the list again
        for k in range(len(numbers)):
            print(numbers[i] + numbers[j] + numbers[k], end=" ")
        print()  # New line after each triplet
    print()  # New line after each pair of triplets
    


# O(2^n)
# runs in exponential time
# the algorithm has a recursive function that calls itself twice for each input
print("\nO(2^n): Fibonacci sequence")

n = 6

def fibonacci(n):
    # Base case: the first two Fibonacci numbers are 0 and 1
    if n <= 1:
        return n
    # Recursive case: the nth Fibonacci number is the sum of the two preceding ones
    return fibonacci(n - 1) + fibonacci(n - 2)

sequence = [fibonacci(i) for i in range(n + 1)]
print(f"Fibonacci sequence up to {n}: {sequence}")