class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { ')' : '(', '}' : '{', ']' : '['
        }

        for S in s:
            if stack and ( S in dic and dic[S] == stack[-1]):
                stack.pop()
            else:
                stack.append(S)
        return not stack
