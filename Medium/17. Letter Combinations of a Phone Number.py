import numpy as np
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        alpha = {'2': ["a", "b", "c"],
                '3': ["d", "e", "f"],
                '4': ["g", "h", "i"],
                '5': ["j", "k", "l"],
                '6': ["m", "n", "o"],
                '7': ["p", "q", "r", "s"],
                '8': ["t", "u", "v"],
                '9': ["w", "x", "y", "z"]
                    }
        combinations = alpha[digits[0]]
        digits = digits[1:]
        for i in digits:
            combinations = [''.join(pair) for pair in product(combinations, alpha[i])] 
                    
        return combinations
