class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = dict() 
        val = 0
        max_val = 0
        left = 0

        for right in range(len(nums)):
            num = nums[right]
            if num in d and d[num] >= left:
                for i in range(left, d[num] + 1):
                    val -= nums[i]
                left = d[num] + 1  
            val += num
            d[num] = right
            max_val = max(max_val, val)

        return max_val

