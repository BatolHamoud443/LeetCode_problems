class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
                k += 1
            else:
                if d[nums[i]] < 2:
                    d[nums[i]] = 2
                    k += 1
                else:
                    nums[i] = 99999
        nums.sort()
        return k
