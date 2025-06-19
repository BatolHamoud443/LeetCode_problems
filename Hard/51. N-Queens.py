class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        D1 = set()
        D2 = set()
        ans = []
        board = [["."] * n for i in range(n)]

        def solutions(r):
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in D1 or (r - c) in D2:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                D1.add(r + c)
                D2.add(r - c)
                

                solutions(r + 1)

                board[r][c] = "."
                cols.remove(c)
                D1.remove(r + c)
                D2.remove(r - c)

        solutions(0)
        return ans
