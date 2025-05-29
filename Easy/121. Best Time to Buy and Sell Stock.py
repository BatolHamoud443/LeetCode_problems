
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        s = []
        while r != len(prices):
            if prices[r] - prices[l] > 0:
                s.append(prices[r] - prices[l])
            else:
                l = r
            r +=1
        if len(s) == 0:
            return 0
        else:
            return max(s)
