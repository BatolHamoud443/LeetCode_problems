class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0]*len(nums)
        for i in range(len(nums)):
            a[i] = max(nums[i], a[i-1]+nums[i])
        return max(a)
        
