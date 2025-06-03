class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        val = 0
        length = +999999
        for r in range(len(nums)):
            val += nums[r]
            while val >= target:
                length = min(length, r-l+1)
                val -= nums[l]
                l +=1
        if length == 999999:
            return 0
        else:
            return length
