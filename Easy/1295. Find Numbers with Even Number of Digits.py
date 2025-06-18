
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            l = str(i)
            if len(l)%2 == 0:
                k += 1
        return k
