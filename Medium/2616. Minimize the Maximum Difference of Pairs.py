class Solution:
    def minimizeMax(self, nums, p):
        nums.sort()
        
        def canFormPairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  
                else:
                    i += 1  
            return count >= p

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if canFormPairs(mid):
                right = mid 
            else:
                left = mid + 1  

        return left

