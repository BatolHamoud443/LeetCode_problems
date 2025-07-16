class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        
        alter_1 = 0
        alter_2 = 0
        for num in nums:
            if num % 2 == 0:
                alter_1 = max(alter_1, alter_2 + 1)
            else:
                alter_2 = max(alter_2, alter_1 + 1)
        
        return max(even, odd, alter_1, alter_2)
