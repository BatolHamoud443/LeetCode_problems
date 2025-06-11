class Solution:
    def scoreOfString(self, s: str) -> int:
        k = 0
        for c in range(1,len(s)):
            k += abs(ord(s[c-1]) - ord(s[c]))
        return k

