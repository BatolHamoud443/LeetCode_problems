class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(min(strs, key=len))
        for i in range(m,-1,-1):
            a = 0
            for j in range(1,len(strs)):
                if strs[j][:i] == strs[0][:i]:
                    a +=1
            
            if a == len(strs)-1:
                return(strs[0][:i])
        if a == 0:
            return ""
