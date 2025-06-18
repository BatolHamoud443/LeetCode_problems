class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        T = {i: [] for i in range(1,7)} 
        B = {i: [] for i in range(1,7)}
        C = {i: 0 for i in range(1,7)}
        for i in range(len(tops)):
            if tops[i] == bottoms[i]:
                C[tops[i]] +=1
            else:
                if tops[i] in T:
                    T[tops[i]].append(i)
                if bottoms[i] in B:
                    B[bottoms[i]].append(i)
        
        ans = 999999
        for i in range(1,7):
            if len(list(set(T[i] + B[i])))+C[i] == len(tops):
                l = min(len(T[i]),len(B[i]))
                if l < ans:
                    ans = l
        if ans == 999999:
            return -1
        else:
            return ans
