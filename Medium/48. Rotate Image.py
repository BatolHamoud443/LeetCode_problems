class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Rotates the matrix 90 degrees clockwise.
        """
        n = len(matrix)
       
        c = [row[:] for row in matrix]

        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 - i] = c[i][j]

