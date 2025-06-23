class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        Map = [[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                Map[i][j] = Map[i-1][j] + Map[i][j-1]
        return Map[-1][-1]
