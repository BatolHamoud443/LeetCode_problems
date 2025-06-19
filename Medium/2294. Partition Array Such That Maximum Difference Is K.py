class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1

        nums.sort()
        ans = []
        l = 0
        i = 1
        ans = 1
        while i < len(nums):
            if nums[i] - nums[l] > k:
                l = i
                ans += 1
            i +=1           
        return ans
        
