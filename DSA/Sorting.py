#%%
"""Bubble Sort"""
# Bubble Sort
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        isSwap = False

        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                isSwap = True
        
        # If no swaps occurred, the array is already sorted
        if not isSwap:
            break
    
    return nums

# Example usage
nums = [324, 342, 324, 4, 23432, 4, 32, 34]
sorted_nums = bubble_sort(nums)
print(sorted_nums)



#%%
"""Insertion Sort"""
# insertion sort
def insertion_sort(nums):
    n= len(nums)
    for i in range(0,n):
        j = i
        while j>0 and nums[j-1]>nums[j]:
            nums[j-1],nums[j]=nums[j],nums[j-1]
            j = j -1
    return nums
print(insertion_sort([324, 342, 324, 4, 23432, 4, 32, 34]))



#%%
"""Selection Sort"""
def selection_sort(nums):
    n=len(nums)
    for i in range(0,n-1):
        min_num=i
        for j in range(i,n):
            if nums[j]<nums[min_num]:
                min_num=j
        nums[min_num],nums[i]=nums[i],nums[min_num]

    return nums
c=selection_sort([5,7,8,4,1,6,9,2])
print(c)



#%%
"""Count Sort"""
# Couting Sort
def counting_sort(nums):
    """
    Performs counting sort on a list of non-negative integers.
    Returns a new sorted list.
    """
    if not nums:
        return []

    # Find the maximum number to determine the size of the frequency array
    mx = max(nums)
    freq = [0] * (mx + 1)

    # Build frequency array
    for x in nums:
        freq[x] += 1

    # Reconstruct sorted array
    sorted_nums = []
    for i in range(mx + 1):
        while freq[i] > 0:
            sorted_nums.append(i)
            freq[i] -= 1

    return sorted_nums


# Example usage
nums = [324, 342, 324, 4, 23432, 4, 32, 34]
sorted_nums = counting_sort(nums)
print(sorted_nums)



#%%
"""Merge Sort"""
# Merge Sort
def merge(nums, l, mid, r):
    """
    Merge function for Merge Sort.
    Merges two sorted subarrays nums[l..mid] and nums[mid+1..r] in place.
    """
    # Create copies of the subarrays
    left = nums[l:mid + 1]
    right = nums[mid + 1:r + 1]

    i = j = 0
    k = l

    # Merge the subarrays back into nums
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements from left
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements from right
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1


def merge_sort(nums, l, r):
    """
    Recursive Merge Sort function.
    Sorts nums[l..r] in place.
    """
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(nums, l, mid)
    merge_sort(nums, mid + 1, r)
    merge(nums, l, mid, r)


def sort_array(nums):
    """
    Main function to sort an array using Merge Sort.
    Returns the sorted array.
    """
    merge_sort(nums, 0, len(nums) - 1)
    return nums


# Example usage
nums = [324, 342, 324, 4, 23432, 4, 32, 34]
sorted_nums = sort_array(nums)
print(sorted_nums)



#%%
"""Quick Sort"""
# Quick Sort
def partition(nums, l, r):
    """
    Partition function for Quick Sort.
    Chooses the last element as pivot and partitions the array.
    """
    pivot = nums[r]
    start = l
    for i in range(l, r + 1):
        if nums[i] <= pivot:
            nums[i], nums[start] = nums[start], nums[i]
            start += 1
    return start - 1


def quick_sort(nums, l, r):
    """
    Recursive Quick Sort function.
    Sorts nums[l..r] in place.
    """
    if l >= r:
        return
    p = partition(nums, l, r)
    quick_sort(nums, l, p - 1)
    quick_sort(nums, p + 1, r)


def sort_array(nums):
    """
    Main function to sort an array using Quick Sort.
    Returns the sorted array.
    """
    quick_sort(nums, 0, len(nums) - 1)
    return nums


# Example usage
nums = [324, 342, 324, 4, 23432, 4, 32, 34]
sorted_nums = sort_array(nums)
print(sorted_nums)



#%%
"""Dutch National Algorithm"""
def sort012(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example
print(sort012([2, 0, 2, 1, 1, 0]))
