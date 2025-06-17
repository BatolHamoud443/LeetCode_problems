class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid),len(grid[0])
        ans = [[float("inf")]*(c+1) for i in range(r+1)]
        ans[r-1][c] = 0
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1, -1):
                ans[i][j] = grid[i][j] + min(ans[i+1][j], ans[i][j+1])
        return ans[0][0]
