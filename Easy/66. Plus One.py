class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int(''.join(map(str, digits)))+1
        ans = str(a)
        out = []
        for c in ans:
            out.append(int(c))
        return out
