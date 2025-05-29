class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.comb(candidates, target, [], ans)
        return ans
    
    def comb(self, nums, target, path, ans):
        if target < 0:
            return 
        if target == 0:
            ans.append(path)
            return 
        for i in range(len(nums)):
            self.comb(nums[i:], target-nums[i], path+[nums[i]], ans)
