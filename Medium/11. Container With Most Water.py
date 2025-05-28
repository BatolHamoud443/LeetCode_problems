class Solution:
    def maxArea(self, height: List[int]) -> int:
        m  = 0
        l = 0
        r = len(height)-1
        while l != r:            
            if m < min(height[l],height[r])*(r-l):
                m = min(height[l],height[r])*(r-l)
#                 print(m)
            if height[l] >= height[r]:
                r -=1
            else:
                l +=1
        return m
