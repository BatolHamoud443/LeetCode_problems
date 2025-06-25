class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()

        def dfs(r,c,k):
            if k == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[k] or (r,c) in visited:
                return False
            visited.add((r,c))
            ans = dfs(r+1,c,k+1) or dfs(r,c+1,k+1) or dfs(r-1,c,k+1) or dfs(r,c-1,k+1)
            visited.remove((r,c))
            return ans

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0) == True:
                    return True
        return False
