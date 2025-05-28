class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0
                k += 1
            else:
                nums[i] = 999
        nums.sort()
        
        return k
