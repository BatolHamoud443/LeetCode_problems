from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a = [[]]*2**(len(nums))
        for i in range(len(a)):
            s = bin(i)[2:]
            s = s[::-1]
            ind = [pos for pos, char in enumerate(s) if char == '1']
            m = []
            for j in ind:
                m.append(nums[j])
            a[i] = m
        return a
