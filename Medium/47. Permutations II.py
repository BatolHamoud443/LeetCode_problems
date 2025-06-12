class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []
        counter = Counter(nums)
        def dfs(res):
            if len(res) == len(nums):
                perms.append(res)
                return 
            
            for c in counter:
                if counter[c]:
                    counter[c]-=1
                    perm = res + [c]
                    dfs(perm)    
                    counter[c]+=1
                
        dfs([])
        return perms
