class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans = 0
        count = 0
        loss = float('inf') 
        for num in nums:
            ans += max(num, num ^ k)
            if (num ^ k) > num:
                count += 1 
            loss = min(loss, abs(num - (num ^ k)))
        if count % 2 == 0:
            return ans  
        else:
            return (ans - loss)
