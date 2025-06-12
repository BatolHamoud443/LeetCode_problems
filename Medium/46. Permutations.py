class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        ans = []
        for _ in range(len(nums)):
            a = nums.pop(0)
            perms = self.permute(nums)
       
            for perm in perms:
                perm.append(a)
            print('p_',perms)
            ans.extend(perms)
            print('a',ans)
            nums.append(a) 
        return ans
