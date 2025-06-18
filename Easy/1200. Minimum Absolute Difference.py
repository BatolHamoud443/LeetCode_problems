from collections import defaultdict
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        arr.sort()
        for i in range(1,len(arr)):
            dis = arr[i] - arr[i-1]
            d[dis].append([arr[i-1],arr[i]])
        a = min(d)
        return d[a]
