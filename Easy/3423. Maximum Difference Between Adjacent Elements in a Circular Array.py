class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(1,len(nums)):
            if abs(nums[i]-nums[i-1]) > res:
                res = abs(nums[i]-nums[i-1])
        return max(res, abs(nums[0]-nums[-1]))
