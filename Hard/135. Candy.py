class Solution:
    def candy(self, ratings: List[int]) -> int:
        k = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                k[i] = k[i-1]+1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                k[i] = max(k[i], k[i+1]+1)
        return sum(k)
