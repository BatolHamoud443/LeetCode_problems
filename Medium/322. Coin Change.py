class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [999999]*(amount+1)
        arr[0] = 0
        for i in range(1,len(arr)):
            for c in coins:
                if i - c >= 0:
                    arr[i] = min(arr[i], arr[i-c]+1)
        if arr[-1] < 999999:
            return arr[-1]
        else:
            return -1
