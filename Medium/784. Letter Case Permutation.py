class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        out = ['']
        for l in s:
            arr = []
            if l.isalpha():
                for o in out:
                    arr.append(o+l.lower())
                    arr.append(o+l.upper())
            else:
                for o in out:
                    arr.append(o+l.lower())
            out = arr
        return out
