class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] - nums[i] > ans:
                    ans = nums[j] - nums[i]
        if ans == 0:
            return -1
        else:
            return ans
