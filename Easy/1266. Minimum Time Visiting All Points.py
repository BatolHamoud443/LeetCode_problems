import numpy as np
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1,len(points)):
            res += max(np.abs(points[i][0]-points[i-1][0]), np.abs(points[i][1]-points[i-1][1]))
        res = int(res)
        return res
