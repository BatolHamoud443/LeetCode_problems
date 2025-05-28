class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
            else:
                k +=1

        nums.sort()
        nums = nums[:k]
        
        return k

