from collections import defaultdict
from typing import List
from math import factorial

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = defaultdict(int) 
        for domino in dominoes:
            
            key = tuple(sorted(domino))
            d[key] += 1 

        k = 0
        for count in d.values():
            if count > 1:
                k += factorial(count) // (factorial(2) * factorial(count - 2))
        
        return k

