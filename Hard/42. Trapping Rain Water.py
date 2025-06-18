class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        L_max = height[L]
        R_max = height[R]
        ans = 0
        while L < R:
            if L_max < R_max:
                L += 1
                L_max = max(L_max, height[L])
                ans += L_max - height[L]
            else:
                R -= 1
                R_max = max(R_max, height[R])
                ans += R_max - height[R]
        
        return ans
