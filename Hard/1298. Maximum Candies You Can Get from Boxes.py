from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque(initialBoxes)
        found = []
        ans = 0
        while q:
            curr = q.popleft()
            if status[curr] == 0:
                found.append(curr)
                continue
            else:
                ans += candies[curr]
                for n in containedBoxes[curr]:
                    q.append(n) 

            for box in keys[curr]:
                status[box] = 1
                if box in found:
                    q.append(box)
                    found.remove(box)        
            
               
        return ans
