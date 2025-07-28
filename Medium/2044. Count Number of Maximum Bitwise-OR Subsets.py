from itertools import combinations
import functools
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        output = sum([list(map(list, combinations(nums, i))) for i in range(len(nums) + 1)], [])
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] +=1
            else:
                dic[n] = 1

        for o in output:
            if len(o) > 1:
                a = reduce(lambda x, y: x | y, o)
                if a in dic:
                    dic[a] +=1
                else:
                    dic[a] = 1
            
        return max(dic.values())
