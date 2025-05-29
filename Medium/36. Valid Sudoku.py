class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res.append((i, element))
                    res.append((element, j))
                    res.append((i // 3, j // 3, element))
        return len(res) == len(set(res))
