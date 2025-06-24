class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        index = [i for i, val in enumerate(nums) if val == key]
        res = set()
        for i in index:
            for j in range(i - k, i + k + 1):
                if 0 <= j < len(nums):
                    res.add(j)
        return sorted(res)
