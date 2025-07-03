class Solution:
    def kthCharacter(self, k: int) -> str:
        m = 0
        while 2**m < k:
            m +=1
        s = 'a'
        for i in range(m):
            for c in s:
                if c == 'z':
                    s = s + 'a'
                else:
                    s = s + (chr(ord(c) + 1))
        return s[k-1]
