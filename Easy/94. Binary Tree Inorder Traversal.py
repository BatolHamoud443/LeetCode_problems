class Solution:
    def maxDifference(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] +=1
            else:
                dic[s[i]] = 1
        
        o = 0
        e = 9999
        for i in dic:
            if dic[i]%2 == 0 and dic[i] < e:
                e = dic[i]
            if dic[i]%2 == 1 and dic[i] > o:
                o = dic[i]
        return o - e  
