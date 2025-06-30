class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        a = nums[0]
        ans = 0
        for key in dic:
            if key - a == 1:
                ans = max(dic[key] + dic[a],ans)
            a = key
        return ans
            
