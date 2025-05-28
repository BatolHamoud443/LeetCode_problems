class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            arr = [0]*(n+1)
            arr[0] = 0
            arr[1] = 1
            arr[2] = 2
            for i in range(3,len(arr)):
                arr[i] = arr[i-1]+arr[i-2]
            return arr[-1]
