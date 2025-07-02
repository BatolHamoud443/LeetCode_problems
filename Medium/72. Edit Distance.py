class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mat = [[float('inf')] * (len(word2)+1) for i in range(len(word1)+1)]
        for i in range(len(word2)+1):
            mat[-1][i] = len(word2) - i
        for i in range(len(word1)+1):
            mat[i][-1] = len(word1) - i
        
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    mat[i][j] = mat[i+1][j+1]
                else:
                    mat[i][j] = 1 + min(mat[i+1][j+1], mat[i][j+1], mat[i+1][j])
        return mat[0][0]
