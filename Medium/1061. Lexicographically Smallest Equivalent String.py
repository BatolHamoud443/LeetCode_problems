from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dic = [] 
        for i in range(len(s1)):
            placed = False
            for row in dic:
                if s1[i] in row or s2[i] in row:
                    row.update([s1[i], s2[i]])
                    placed = True
                    break
            if not placed:
                dic.append(set([s1[i], s2[i]]))

        merged = []
        for group in dic:
            for m in merged:
                if group & m:
                    m.update(group)
                    break
            else:
                merged.append(group)
        l = ''
        for i in baseStr:
            f = False
            for row in merged:
                if i in row:
                    l = l + min(list(row))
                    f = True
            if f == False:
                l = l+i
        return l

