class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        occurrences = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    occurrences.append((i, j))
        
        for i,j in occurrences:
            matrix[i] = [0] * len(matrix[i])
            for row in matrix:
                row[j] = 0
                

