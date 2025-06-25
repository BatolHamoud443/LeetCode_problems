from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_str = []
        for s in strs:
            new_str.append(''.join(sorted(s.lower())))
        dic = defaultdict(list)
        for i in range(len(new_str)):
            dic[new_str[i]].append(i)
        
        ans = []
        for i in dic:
            res = []
            for j in dic[i]:
                res.append(strs[j])
            ans.append(res)
        return ans
