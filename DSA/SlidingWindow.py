class Solution:
    """finding subarray of maximum average"""
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==1:
            return nums[0]/k
            
        wind_sum = sum(nums[0:k])
        max_sum = wind_sum

        for i in range(k, len(nums)):
            wind_sum -= nums[i-k]
            wind_sum += nums[i]
            max_sum = max(max_sum, wind_sum)
        return max_sum/k  

    """Finding the length longest subarray without repeating the characters"""
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length=0
        i=0
        charSet = set()

        for j in range(n):
            while s[j] in charSet:
                charSet.remove(s[i])
                i+=1
            
            charSet.add(s[j])
            max_length = max(max_length, j-i+1)
        
        return max_length

output = Solution()

print("="*40)
print(
    f"max subarray average of k length is: "
    f"{output.findMaxAverage([1,12,-5,-6,50,3], 4)}"
)
print("="*40)
print()

print("="*40)
print(
    f"longest length of the subarray:"
    f"{output.lengthOfLongestSubstring("abcabcbb")}"
)
print("="*40)
print()