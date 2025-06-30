class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                
                if board[i][j] != '.':
                    n = int(board[i][j])
                    rows[i].add(n)
                    cols[j].add(n)
                    l = i//3 * 3 + j//3
                    box[l].add(n)
        
        def back_track(i,j):    
            nonlocal flag
            if i == 9:
                flag = True
                return

            new_i = i + (j+1)//9
            new_j = (j+1)%9

            if board[i][j] != '.':
                back_track(new_i, new_j)

            else:
                for num in range(1,10):
                    l = i//3 * 3 + j//3
                    if num not in rows[i] and num not in cols[j] and num not in box[l]:
                        
                        rows[i].add(num)
                        cols[j].add(num)
                        box[l].add(num)
                        board[i][j] = str(num)
                        back_track(new_i, new_j)
                        
                        if not flag:
                            rows[i].remove(num)
                            cols[j].remove(num)
                            box[l].remove(num)
                            board[i][j] = '.'

        flag = False
        back_track(0,0)
