class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        if set(nums) == {0}:
            return [[0,0,0]]
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                v = nums[i] + nums[l] + nums[r]
                if v > 0:
                    r = r - 1
                elif v < 0:
                    l = l + 1
                else:
                    out.append([nums[i], nums[l], nums[r]])
                    l = l+1
                    while l < r and nums[l] == nums[l-1]:
                        l = l+1
                    
        return out
