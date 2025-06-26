class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        val = 0
        i = 0
        while i < min(len(s), 32):
            if s[len(s) - i - 1] == '1':
                if val + 2 ** i > k:
                    break
                val += 2 ** i
            i += 1

        removed_count = 0
        while i < len(s):
            if s[len(s) - i - 1] == '1':
                removed_count += 1
            i += 1
        return len(s) - removed_count
