class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        def dfs(cur, n, ans):
            if cur > n:
                return
            ans.append(cur)
            for i in range(0,10):
                dfs(cur*10+i,n,ans)

        ans = []
        for i in range(1,10):
            dfs(i,n,ans)
        return ans

        
