class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cor = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        Map = [[0]*n for _ in range(m)]
        Map[0][0] = 1  


        for i in range(1, m):
            if obstacleGrid[i][0] == 0 and Map[i-1][0] == 1:
                Map[i][0] = 1

        for j in range(1, n):
            if obstacleGrid[0][j] == 0 and Map[0][j-1] == 1:
                Map[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    Map[i][j] = Map[i-1][j] + Map[i][j-1]

        return Map[-1][-1]

