from itertools import groupby
class Solution:
    def possibleStringCount(self, word: str) -> int:
        clusters = [''.join(group) for key, group in groupby(word)]
        ans = 1
        for i in range(len(clusters)):
            ans += len(clusters[i])-1
        return ans
