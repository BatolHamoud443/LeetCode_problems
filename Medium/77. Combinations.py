import numpy as np
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a = []
        nums = []
        for i in range(n):
            nums.append(i+1)
        for i in range(2**(len(nums))):
            s = bin(i)[2:]
            s = s[::-1]
            ind = [pos for pos, char in enumerate(s) if char == '1']
            if len(ind) == k:
                m = []
                for j in ind:
                    m.append(nums[j])
                a.append(m)
        return a
