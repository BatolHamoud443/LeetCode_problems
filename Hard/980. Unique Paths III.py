class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
        empty = 0 
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 1: 
                    x = i
                    y = j
                elif grid[i][j] == 0: 
                    empty += 1 
        self.ans = 0

        def dfs(i, j, empty):     
            if grid[i][j] == 2: 
                if empty == -1: 
                    self.ans += 1
                return 
            grid[i][j] = -1 
            for r, c in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= r < m and 0 <= c < n and grid[r][c] != -1: 
                    dfs(r, c, empty-1)
            grid[i][j] = 0 


        dfs(x, y, empty)
        return self.ans
