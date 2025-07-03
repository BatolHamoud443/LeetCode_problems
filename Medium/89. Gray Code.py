class Solution:
    def grayCode(self, n: int) -> List[int]:
        base = [0,1]
        for i in range(1,n):
            for j in range(len(base)-1,-1,-1):
                print(base[j])
                base.append(base[j] + 2**i)
        return base
