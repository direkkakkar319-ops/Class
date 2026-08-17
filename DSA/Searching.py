#%%
"""Linear Search"""
def Linear_Search(arr,target):
    n=len(arr)

    for i in range(n):
        if arr[i]==target:
            return f"{target} found at {i}"
nums=[244,324,43,24,32432,432,432432,4432,432,43242,323,3242,324234,323,43,434,32,5767,9,345879,7532556,84,543634,68,324,32,56346]
num=int(input("enter the number to be found")) 
print(Linear_Search(nums,num))



#%%
"""Simple Binary Search"""
def binary_search(nums,target):
    n=len(nums)
    low , high = 0 , n-1

    while low<=high:
        mid=(low + high) // 2
        if nums[mid] == target:
            return f"emement found at: {mid}"
        
        elif nums[mid]>target:
            high = mid - 1
        
        else:
            low = mid + 1

print(binary_search([1,2,3,5,6,7,8,9,10,11,12,13,14,15,16], 16))



#%%
"""binary search for rotated sorted array having distinct numbers only"""
def Bin_search_rotated_sorted(nums,target):
    n = len(nums)
    low , high = 0 , n-1
    while low <= high :
        mid = ( low + high ) // 2

        if nums[mid] == target:
            return f"element found at index:{mid}"
        
        if nums[low]<nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            
            else:
                high = mid - 1
    
    return "element not found"

print(Bin_search_rotated_sorted([2,5,6,0,1],1))



#%%
"""integer square root of a number using Binary Search"""
def mySqrt(x):
    left, right = 0, x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            left = mid + 1
        else:
            right = mid - 1

    return right



# %%
"""removes duplicate elements from a sorted array"""
def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
    